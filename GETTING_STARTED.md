# Getting Started with BABA 🚀

Welcome! Follow these simple steps to get BABA up and running.

---

## Step 1: Add Your OpenAI API Key ⚡

**This is the ONLY required setup step!**

1. Open the file `.env` in the BABA folder
2. Find this line:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Replace `your_openai_api_key_here` with your actual OpenAI API key

**Don't have an API key yet?**
- Visit: https://platform.openai.com/api-keys
- Sign up or log in
- Create a new API key
- Copy and paste it into `.env`

---

## Step 2: Install Dependencies 📦

Open your terminal/command prompt in the BABA folder and run:

```bash
pip install -r requirements.txt
```

This will install all required packages (takes 2-3 minutes).

---

## Step 3: Verify Setup (Optional but Recommended) ✅

Run the verification script to check everything is working:

```bash
python verify_setup.py
```

This will check:
- ✓ Python version
- ✓ Dependencies installed
- ✓ API key configured
- ✓ All files present
- ✓ API connection working

---

## Step 4: Run BABA 🎉

### Option A: Use the Run Script (Easiest)

**On Windows:**
```bash
run.bat
```

**On Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

### Option B: Manual Start

```bash
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501`

---

## First Test 🧪

Try these examples:

### Test 1: Ask for an Explanation
Type in the input box:
```
What is critical thinking?
```

Click "Submit to BABA" and you should see:
- Bilingual explanation (English + Arabic)
- A Gulf-region example
- An auto-generated quiz
- Next steps suggestions

### Test 2: Get Writing Help
Paste this text:
```
The research is show that climate change effect economy.
```

Click "Submit to BABA" and you should see:
- Corrected text
- Arabic explanation of changes
- Grammar points
- Writing tips

---

## Understanding the Interface 🖥️

### Main Area
- **Input Box**: Type questions or paste text to improve
- **Submit Button**: Process your request
- **Results**: Bilingual explanations, corrections, quizzes

### Sidebar
- **About**: Information about BABA
- **Examples**: Sample inputs
- **Session Stats**: Your progress
- **Clear Session**: Reset everything

### Autonomous Actions
- Click "Autonomous Agent Actions" to see how BABA thinks
- Watch the multi-step decision-making process

---

## Troubleshooting 🔧

### "Configuration Error: OPENAI_API_KEY not set!"
**Problem**: API key not configured
**Solution**: Edit `.env` and add your real API key

### "ModuleNotFoundError"
**Problem**: Dependencies not installed
**Solution**: Run `pip install -r requirements.txt`

### App starts but nothing happens
**Problem**: Could be API key or internet
**Solution**:
1. Check your internet connection
2. Verify API key is valid
3. Check if you have API credits

### Arabic text looks strange
**Problem**: Terminal encoding
**Solution**: This is normal - Arabic will display correctly in the browser

---

## What's Next? 🎯

### Explore Features
- Try different questions
- Test various writing samples
- Take the quizzes
- Check the autonomous actions

### Deploy Online (Optional)
- See `DEPLOYMENT.md` for full instructions
- Streamlit Cloud is free and takes 5 minutes
- Share with others!

### Customize (Optional)
- Edit prompts in `prompts/` folder
- Modify agents in `agents/` folder
- Adjust UI in `app.py`

---

## Need More Help? 📚

Check these documents:
- **README.md** - Complete technical documentation
- **QUICKSTART.md** - Quick reference guide
- **DEPLOYMENT.md** - Deployment instructions
- **PROJECT_SUMMARY.md** - Complete project overview

---

## Quick Commands Reference

```bash
# Verify setup
python verify_setup.py

# Test agents
python test_agents.py

# Run application
streamlit run app.py

# Or use run scripts
run.bat        # Windows
./run.sh       # Mac/Linux
```

---

## That's It! 🎉

You're ready to use BABA. The complete setup takes less than 5 minutes.

**Questions?** All documentation is in the BABA folder.

**Ready to deploy?** See DEPLOYMENT.md for instructions.

---

**Happy Learning! 🎓**
