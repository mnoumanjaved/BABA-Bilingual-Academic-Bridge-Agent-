# BABA Quick Start Guide 🚀

Get BABA up and running in 5 minutes!

## ⚡ Fast Track Setup

### Step 1: Add Your OpenAI API Key (30 seconds)

Open the `.env` file in the BABA folder and replace the placeholder with your actual API key:

```env
OPENAI_API_KEY=sk-your-actual-openai-api-key-here
```

**Where to get an API key:**
- Go to [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Create a new API key
- Copy and paste it into the `.env` file

### Step 2: Install Dependencies (2-3 minutes)

Open your terminal/command prompt in the BABA folder:

```bash
# Create virtual environment (optional but recommended)
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### Step 3: Run BABA (10 seconds)

```bash
streamlit run app.py
```

Your default browser will automatically open to `http://localhost:8501` 🎉

---

## ✅ First Test

Try these examples to test BABA:

### Example 1: Ask for an Explanation
Type: **"What is critical thinking?"**

You should see:
- ✅ Bilingual explanation (English + Arabic)
- ✅ Gulf-region example
- ✅ Auto-generated quiz
- ✅ Learning suggestions

### Example 2: Submit Text for Improvement
Paste: **"The research is show that climate change effect economy."**

You should see:
- ✅ Corrected academic text
- ✅ Arabic explanation of changes
- ✅ Grammar points highlighted
- ✅ Next steps suggested

---

## 🎯 Understanding the Interface

### Main Input Area
- Type questions OR paste text to improve
- Works with English, Arabic, or mixed text
- Click "Submit to BABA" to process

### Sidebar
- View session statistics
- See quiz scores
- Access examples
- Clear session

### Autonomous Actions Panel
- Expand to see how BABA thinks
- Shows agent decision-making
- Demonstrates multi-step reasoning

---

## 🔧 Troubleshooting

### "Configuration Error: OPENAI_API_KEY not set!"
**Fix**: Edit `.env` file and add your real API key

### "ModuleNotFoundError"
**Fix**: Run `pip install -r requirements.txt`

### Arabic text looks weird
**Fix**: This is normal in some terminals - it will display correctly in the browser

### App loads but nothing happens when I click submit
**Fix**: Check your internet connection and API key validity

---

## 💡 Tips for Best Results

1. **For Explanations:**
   - Ask specific questions
   - One concept at a time
   - Use simple language

2. **For Writing Improvement:**
   - Submit 1-3 paragraphs at a time
   - Academic writing works best
   - Clear, complete sentences

3. **For Quizzes:**
   - Take the quiz after explanations
   - Read both English and Arabic questions
   - Review incorrect answers

---

## 📊 What's Happening Behind the Scenes?

When you submit input:
1. **Task Classifier** determines what you need
2. **Orchestrator** routes to the right agent
3. **Specialized Agents** process your request:
   - Explainer: Creates bilingual explanations
   - Writer: Improves your writing
   - Quiz: Generates comprehension tests
4. **Feedback Agent** suggests next steps
5. **All agents coordinate autonomously**

---

## 🎓 Educational Use Cases

### For Students:
- Understand difficult concepts
- Improve academic English
- Test comprehension
- Learn from mistakes

### For Instructors:
- Demonstrate AI agents
- Support bilingual learners
- Create quiz questions
- Provide writing feedback

---

## 📱 Next Steps

Once everything works:

1. ✅ **Explore Features**
   - Try different questions
   - Test writing samples
   - Take quizzes

2. ✅ **Deploy Online** (Optional)
   - See `DEPLOYMENT.md` for instructions
   - Streamlit Cloud is free and easy
   - Share with others

3. ✅ **Customize** (Optional)
   - Edit prompts in `prompts/` folder
   - Adjust agent behavior
   - Modify UI in `app.py`

---

## 🎬 Demo Video Script

Record a 30-60 second video showing:

1. **Opening** (5s): "This is BABA, a bilingual academic AI agent"
2. **Explanation Example** (20s): Type question → Show bilingual response
3. **Writing Example** (20s): Paste text → Show improvements
4. **Quiz** (10s): Show auto-generated quiz
5. **Closing** (5s): "Autonomous, bilingual, academic support"

---

## 🆘 Need Help?

Check these resources:
- `README.md` - Full documentation
- `DEPLOYMENT.md` - Deployment guides
- Streamlit docs: [docs.streamlit.io](https://docs.streamlit.io)
- OpenAI docs: [platform.openai.com/docs](https://platform.openai.com/docs)

---

## ✨ You're Ready!

BABA is now running and ready to help bilingual students succeed! 🎓

**Pro tip**: Press `Ctrl+C` in the terminal to stop the app when you're done.
