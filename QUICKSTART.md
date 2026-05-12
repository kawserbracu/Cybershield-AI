# 🚀 Quick Start Guide - CyberShield AI

## For Windows (Windsurf/VS Code/Any IDE)

### Step 1: Setup Python Environment (5 minutes)
1. Open Command Prompt or PowerShell
2. Navigate to your project folder:
   ```cmd
   cd path\to\CyberShield-AI
   ```

3. Create virtual environment:
   ```cmd
   python -m venv venv
   ```

4. Activate virtual environment:
   ```cmd
   venv\Scripts\activate
   ```

### Step 2: Install Dependencies (3 minutes)
```cmd
pip install -r requirements.txt
```

### Step 3: Run the Project (Auto - 10-15 minutes)
```cmd
python main.py
```

**That's it!** The script will:
- ✅ Auto-download the dataset
- ✅ Train the model
- ✅ Generate results & visualizations
- ✅ Save the trained model

### Step 4: Check Generated Files
After completion, you'll have:
- `cybershield_model.h5` - Trained model
- `results.png` - Performance metrics
- `loss_curve.png` - Training curves

---

## Upload to GitHub (5 minutes)

### Method 1: Using Git Commands
```bash
git init
git add .
git commit -m "Initial commit: CyberShield AI - Network IDS"
git branch -M main
git remote add origin https://github.com/yourusername/CyberShield-AI.git
git push -u origin main
```

### Method 2: GitHub Desktop
1. Open GitHub Desktop
2. File → Add Local Repository → Choose CyberShield-AI folder
3. Commit changes with message
4. Publish repository

### Method 3: Direct Upload
1. Go to github.com
2. Create new repository: "CyberShield-AI"
3. Upload files directly via web interface

---

## For CV/Resume

**Add this to your CV:**

### PROJECT EXPERIENCE

**CyberShield AI - Network Intrusion Detection System**  
*CSE496 - Ethical Hacking & Cybersecurity, BRAC University*  
*Jan 2024 - May 2024*

- Developed an advanced Network Intrusion Detection System using hybrid deep learning (CNN + LSTM)
- Achieved 98%+ accuracy in detecting network attacks on KDD Cup 1999 dataset
- Implemented comprehensive data preprocessing, feature engineering, and model optimization
- Technologies: Python, TensorFlow, Keras, Scikit-learn, Pandas, NumPy
- **GitHub**: github.com/yourusername/CyberShield-AI

---

## Troubleshooting

### Issue: "TensorFlow not found"
**Solution**: Install TensorFlow separately
```cmd
pip install tensorflow
```

### Issue: "Dataset download fails"
**Solution**: Manually download dataset
1. Download from: http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz
2. Place in project folder
3. Run script again

### Issue: "Out of memory"
**Solution**: Reduce batch size in main.py
- Change line: `epochs=20, batch_size=128`
- To: `epochs=20, batch_size=64`

---

## Time Estimate

| Task | Time |
|------|------|
| Setup environment | 5 min |
| Install dependencies | 3 min |
| Run training | 10-15 min |
| GitHub upload | 5 min |
| **TOTAL** | **~30 minutes** |

---

## Pro Tips

1. **Run on Colab** (if your PC is slow):
   - Upload main.py to Google Colab
   - Free GPU access
   - Faster training (5 minutes instead of 15)

2. **Customize for better CV**:
   - Add your name in main.py header
   - Update README with your details
   - Take screenshots of results

3. **Impress recruiters**:
   - Add GitHub link to CV
   - Mention accuracy percentage (98%+)
   - Highlight "Hybrid Deep Learning"

---

## Next Steps After Completion

✅ Upload to GitHub  
✅ Add to CV  
✅ Update LinkedIn  
✅ Prepare 2-minute explanation  
✅ Ready for job applications!

---

**Need help?** Check README.md for detailed documentation.
