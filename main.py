"""
CyberShield AI - Advanced Network Intrusion Detection System
Author: Your Name
Course: CSE496 - Ethical Hacking & Cybersecurity
Institution: BRAC University

Description: Hybrid Deep Learning model (CNN + LSTM) for real-time network intrusion detection
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("🛡️  CyberShield AI - Network Intrusion Detection System")
print("=" * 70)

class CyberShieldAI:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.history = None
        
    def load_and_preprocess_data(self, filepath='kddcup.data_10_percent.gz'):
        """Load and preprocess the KDD Cup dataset"""
        print("\n[1/6] Loading dataset...")
        
        # Column names for KDD Cup dataset
        columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes',
                   'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
                   'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',
                   'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
                   'num_access_files', 'num_outbound_cmds', 'is_host_login',
                   'is_guest_login', 'count', 'srv_count', 'serror_rate',
                   'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
                   'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
                   'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
                   'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
                   'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
                   'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
                   'dst_host_srv_rerror_rate', 'label']
        
        try:
            df = pd.read_csv(filepath, names=columns)
        except:
            print("⚠️  Dataset not found. Downloading...")
            url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'
            df = pd.read_csv(url, names=columns)
        
        print(f"   ✓ Loaded {len(df)} records")
        
        # Binary classification: Normal vs Attack
        df['binary_label'] = df['label'].apply(lambda x: 0 if x == 'normal.' else 1)
        
        print(f"   ✓ Normal traffic: {len(df[df['binary_label']==0])}")
        print(f"   ✓ Attack traffic: {len(df[df['binary_label']==1])}")
        
        return df
    
    def feature_engineering(self, df):
        """Feature engineering and encoding"""
        print("\n[2/6] Feature engineering...")
        
        # Select features
        categorical_cols = ['protocol_type', 'service', 'flag']
        numeric_cols = [col for col in df.columns if col not in categorical_cols + ['label', 'binary_label']]
        
        # One-hot encoding for categorical features
        df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
        
        # Separate features and labels
        X = df_encoded.drop(['label', 'binary_label'], axis=1)
        y = df_encoded['binary_label'].values
        
        print(f"   ✓ Feature dimensions: {X.shape}")
        print(f"   ✓ Total features: {X.shape[1]}")
        
        return X.values, y
    
    def prepare_data(self, X, y, test_size=0.2):
        """Split and normalize data"""
        print("\n[3/6] Preparing data...")
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42, stratify=y
        )
        
        # Normalize features
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)
        
        # Reshape for CNN-LSTM (samples, timesteps, features)
        n_features = X_train.shape[1]
        X_train = X_train.reshape(X_train.shape[0], 1, n_features)
        X_test = X_test.reshape(X_test.shape[0], 1, n_features)
        
        print(f"   ✓ Training samples: {X_train.shape[0]}")
        print(f"   ✓ Testing samples: {X_test.shape[0]}")
        
        return X_train, X_test, y_train, y_test
    
    def build_hybrid_model(self, input_shape):
        """Build CNN-LSTM Hybrid Deep Learning Model"""
        print("\n[4/6] Building Hybrid CNN-LSTM model...")
        
        model = models.Sequential([
            # CNN Layer for feature extraction
            layers.Conv1D(filters=64, kernel_size=1, activation='relu', input_shape=input_shape),
            layers.MaxPooling1D(pool_size=1),
            layers.Dropout(0.3),
            
            # LSTM Layer for temporal patterns
            layers.LSTM(64, return_sequences=True),
            layers.Dropout(0.3),
            layers.LSTM(32),
            layers.Dropout(0.3),
            
            # Dense layers
            layers.Dense(64, activation='relu'),
            layers.Dropout(0.3),
            layers.Dense(32, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ])
        
        model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy', tf.keras.metrics.Precision(), tf.keras.metrics.Recall()]
        )
        
        print("   ✓ Model architecture:")
        model.summary()
        
        self.model = model
        return model
    
    def train_model(self, X_train, y_train, X_test, y_test, epochs=20, batch_size=128):
        """Train the model"""
        print("\n[5/6] Training model...")
        
        # Early stopping callback
        early_stopping = keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=5,
            restore_best_weights=True
        )
        
        # Train
        self.history = self.model.fit(
            X_train, y_train,
            validation_data=(X_test, y_test),
            epochs=epochs,
            batch_size=batch_size,
            callbacks=[early_stopping],
            verbose=1
        )
        
        print("   ✓ Training completed!")
        
        return self.history
    
    def evaluate_model(self, X_test, y_test):
        """Evaluate model performance"""
        print("\n[6/6] Evaluating model...")
        
        # Predictions
        y_pred_prob = self.model.predict(X_test)
        y_pred = (y_pred_prob > 0.5).astype(int).flatten()
        
        # Metrics
        accuracy = accuracy_score(y_test, y_pred)
        
        print("\n" + "=" * 70)
        print("📊 MODEL PERFORMANCE")
        print("=" * 70)
        print(f"\n🎯 Accuracy: {accuracy*100:.2f}%")
        print("\n📋 Classification Report:")
        print(classification_report(y_test, y_pred, target_names=['Normal', 'Attack']))
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        
        return accuracy, cm, y_pred
    
    def plot_results(self, cm):
        """Visualize results"""
        print("\n📈 Generating visualizations...")
        
        # Create figure with subplots
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        
        # Plot 1: Training History
        axes[0].plot(self.history.history['accuracy'], label='Train Accuracy', linewidth=2)
        axes[0].plot(self.history.history['val_accuracy'], label='Val Accuracy', linewidth=2)
        axes[0].set_title('Model Accuracy Over Epochs', fontsize=14, fontweight='bold')
        axes[0].set_xlabel('Epoch')
        axes[0].set_ylabel('Accuracy')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Plot 2: Confusion Matrix
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[1],
                    xticklabels=['Normal', 'Attack'],
                    yticklabels=['Normal', 'Attack'])
        axes[1].set_title('Confusion Matrix', fontsize=14, fontweight='bold')
        axes[1].set_ylabel('True Label')
        axes[1].set_xlabel('Predicted Label')
        
        plt.tight_layout()
        plt.savefig('results.png', dpi=300, bbox_inches='tight')
        print("   ✓ Saved results.png")
        
        # Plot Loss
        plt.figure(figsize=(10, 5))
        plt.plot(self.history.history['loss'], label='Train Loss', linewidth=2)
        plt.plot(self.history.history['val_loss'], label='Val Loss', linewidth=2)
        plt.title('Model Loss Over Epochs', fontsize=14, fontweight='bold')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig('loss_curve.png', dpi=300, bbox_inches='tight')
        print("   ✓ Saved loss_curve.png")
        
        plt.show()
    
    def save_model(self, filepath='cybershield_model.h5'):
        """Save trained model"""
        self.model.save(filepath)
        print(f"\n💾 Model saved as {filepath}")


def main():
    # Initialize CyberShield AI
    ids = CyberShieldAI()
    
    # Load data
    df = ids.load_and_preprocess_data()
    
    # Feature engineering
    X, y = ids.feature_engineering(df)
    
    # Prepare data
    X_train, X_test, y_train, y_test = ids.prepare_data(X, y)
    
    # Build model
    input_shape = (X_train.shape[1], X_train.shape[2])
    ids.build_hybrid_model(input_shape)
    
    # Train model
    ids.train_model(X_train, y_train, X_test, y_test, epochs=20)
    
    # Evaluate
    accuracy, cm, y_pred = ids.evaluate_model(X_test, y_test)
    
    # Plot results
    ids.plot_results(cm)
    
    # Save model
    ids.save_model()
    
    print("\n" + "=" * 70)
    print("✅ CyberShield AI - Project Completed Successfully!")
    print("=" * 70)
    print("\n📂 Generated files:")
    print("   • cybershield_model.h5 (trained model)")
    print("   • results.png (performance metrics)")
    print("   • loss_curve.png (training curves)")
    print("\n🚀 Ready for deployment!")


if __name__ == "__main__":
    main()
