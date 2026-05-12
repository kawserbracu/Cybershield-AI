# 🛡️ CyberShield AI - Advanced Network Intrusion Detection System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**An advanced hybrid deep learning system combining CNN and LSTM for real-time network intrusion detection with 98%+ accuracy.**

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Dataset](#dataset)
- [Technologies](#technologies)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Overview

**CyberShield AI** is an intelligent Network Intrusion Detection System (NIDS) developed as part of **CSE496 - Ethical Hacking & Cybersecurity** course at BRAC University. The system leverages a **hybrid deep learning architecture** combining:

- **Convolutional Neural Networks (CNN)** for spatial feature extraction
- **Long Short-Term Memory (LSTM)** networks for temporal pattern recognition
- **Advanced preprocessing** with feature engineering and normalization

This hybrid approach achieves **superior detection accuracy** compared to traditional machine learning methods and simple neural networks.

---

## ✨ Features

### Core Capabilities
- ✅ **Hybrid Deep Learning Model** - CNN + LSTM architecture
- ✅ **High Accuracy** - 98%+ detection rate for network attacks
- ✅ **Binary Classification** - Distinguishes between normal traffic and attacks
- ✅ **Comprehensive Preprocessing** - Feature engineering, normalization, and encoding
- ✅ **Real-time Compatible** - Optimized for streaming data processing
- ✅ **Visualization Suite** - Training curves, confusion matrices, and performance metrics
- ✅ **Model Persistence** - Save and load trained models

### Technical Highlights
- Early stopping to prevent overfitting
- Dropout layers for regularization
- Stratified train-test split for balanced evaluation
- Automated feature encoding for categorical variables
- GPU acceleration support (CUDA compatible)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT LAYER                              │
│                  (Network Traffic Data)                      │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│              PREPROCESSING MODULE                            │
│  • Feature Engineering    • One-Hot Encoding                 │
│  • Normalization          • Dimensionality Handling          │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                  CNN LAYER (Feature Extraction)              │
│  • Conv1D (64 filters)    • MaxPooling1D                     │
│  • ReLU Activation        • Dropout (0.3)                    │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│              LSTM LAYERS (Temporal Patterns)                 │
│  • LSTM (64 units, return_sequences=True)                    │
│  • LSTM (32 units)                                           │
│  • Dropout (0.3 each)                                        │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                  DENSE LAYERS                                │
│  • Dense (64, ReLU)       • Dense (32, ReLU)                 │
│  • Dropout (0.3)          • Output (1, Sigmoid)              │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                  OUTPUT LAYER                                │
│            Binary Classification: Normal / Attack            │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- (Optional) CUDA-capable GPU for faster training

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/CyberShield-AI.git
cd CyberShield-AI
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Download Dataset (Automatic)
The script automatically downloads the KDD Cup 1999 dataset on first run. Alternatively, manually download:
```bash
wget http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz
```

---

## 💻 Usage

### Basic Usage
```bash
python main.py
```

### Expected Output
```
======================================================================
🛡️  CyberShield AI - Network Intrusion Detection System
======================================================================

[1/6] Loading dataset...
   ✓ Loaded 494021 records
   ✓ Normal traffic: 97278
   ✓ Attack traffic: 396743

[2/6] Feature engineering...
   ✓ Feature dimensions: (494021, 122)
   ✓ Total features: 122

[3/6] Preparing data...
   ✓ Training samples: 395216
   ✓ Testing samples: 98805

[4/6] Building Hybrid CNN-LSTM model...
   ✓ Model architecture:
   [Model summary displayed here]

[5/6] Training model...
   [Training progress with accuracy metrics]
   ✓ Training completed!

[6/6] Evaluating model...

======================================================================
📊 MODEL PERFORMANCE
======================================================================

🎯 Accuracy: 98.45%

📋 Classification Report:
              precision    recall  f1-score   support

      Normal       0.96      0.95      0.95     19455
      Attack       0.99      0.99      0.99     79350

    accuracy                           0.98     98805
```

---

## 📊 Results

### Performance Metrics
| Metric | Score |
|--------|-------|
| **Accuracy** | 98.45% |
| **Precision (Attack)** | 99% |
| **Recall (Attack)** | 99% |
| **F1-Score (Attack)** | 99% |
| **Training Time** | ~5 minutes (GPU) / ~15 minutes (CPU) |

### Visualizations
![Results](results.png)
*Training accuracy and confusion matrix*

![Loss Curve](loss_curve.png)
*Training and validation loss over epochs*

---

## 📦 Dataset

### KDD Cup 1999 Dataset
- **Source**: [UCI KDD Archive](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)
- **Records**: 494,021 network connections
- **Features**: 41 attributes (numerical + categorical)
- **Classes**: Binary (Normal vs. Attack)

### Attack Types Included
- **DoS** (Denial of Service): smurf, neptune, back, teardrop, pod, land
- **Probe**: satan, ipsweep, nmap, portsweep
- **R2L** (Remote to Local): warezclient, guess_passwd, warezmaster, imap, ftp_write, multihop, phf, spy
- **U2R** (User to Root): buffer_overflow, rootkit, loadmodule, perl

---

## 🛠️ Technologies

### Core Technologies
- **Python 3.8+** - Primary programming language
- **TensorFlow 2.x / Keras** - Deep learning framework
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation
- **Scikit-learn** - Preprocessing and metrics

### Visualization
- **Matplotlib** - Plotting and charts
- **Seaborn** - Statistical visualizations

### Development Tools
- **Jupyter Notebook** - Interactive development
- **Git** - Version control

---

## 🔮 Future Enhancements

- [ ] **Multi-class Classification** - Identify specific attack types (DoS, Probe, R2L, U2R)
- [ ] **Real-time Streaming** - Integration with Apache Kafka for live traffic analysis
- [ ] **Web Dashboard** - Flask/FastAPI backend with React frontend
- [ ] **Model Explainability** - SHAP values and LIME for interpretability
- [ ] **Edge Deployment** - Optimize for Raspberry Pi / IoT devices
- [ ] **Ensemble Methods** - Combine with Random Forest and XGBoost
- [ ] **Adversarial Robustness** - Defense against adversarial attacks
- [ ] **Federated Learning** - Privacy-preserving distributed training

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Contact

**Your Name**  
📧 Email: your.email@g.bracu.ac.bd  
🔗 LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)  
🐙 GitHub: [@yourusername](https://github.com/yourusername)

**Course**: CSE496 - Ethical Hacking & Cybersecurity  
**Institution**: BRAC University  
**Year**: 2024

---

## 🙏 Acknowledgments

- BRAC University - CSE496 Course
- KDD Cup 1999 Dataset contributors
- TensorFlow and Keras communities
- Open-source cybersecurity community

---

## 📈 Project Stats

![GitHub stars](https://img.shields.io/github/stars/yourusername/CyberShield-AI?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/CyberShield-AI?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/CyberShield-AI?style=social)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for Cybersecurity

</div>
