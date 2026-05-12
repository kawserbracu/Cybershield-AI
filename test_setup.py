"""
Quick Test Script - Verify CyberShield AI Setup
Run this before main.py to check if everything is installed correctly
"""

import sys

def test_imports():
    """Test if all required packages are installed"""
    print("Testing package installations...\n")
    
    packages = {
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'matplotlib': 'Matplotlib',
        'seaborn': 'Seaborn',
        'sklearn': 'Scikit-learn',
        'tensorflow': 'TensorFlow'
    }
    
    failed = []
    
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✓ {name} - OK")
        except ImportError:
            print(f"✗ {name} - MISSING")
            failed.append(name)
    
    print("\n" + "="*50)
    
    if not failed:
        print("✅ All packages installed successfully!")
        print("\nYou can now run: python main.py")
        return True
    else:
        print(f"❌ Missing packages: {', '.join(failed)}")
        print("\nTo install missing packages, run:")
        print("pip install -r requirements.txt")
        return False


def test_tensorflow():
    """Test TensorFlow GPU availability"""
    try:
        import tensorflow as tf
        print("\n" + "="*50)
        print("TensorFlow Configuration:")
        print(f"Version: {tf.__version__}")
        print(f"GPU Available: {len(tf.config.list_physical_devices('GPU')) > 0}")
        
        if len(tf.config.list_physical_devices('GPU')) > 0:
            print("✅ GPU acceleration enabled!")
        else:
            print("ℹ️  Running on CPU (slower but works fine)")
    except:
        pass


if __name__ == "__main__":
    print("="*50)
    print("CyberShield AI - Installation Test")
    print("="*50 + "\n")
    
    if test_imports():
        test_tensorflow()
        print("\n" + "="*50)
        print("🚀 Ready to go!")
        print("="*50)
    else:
        print("\n" + "="*50)
        print("⚠️  Please install missing packages first")
        print("="*50)
        sys.exit(1)
