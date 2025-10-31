# BABA - Bilingual Academic Bridge Agent 🎓

An autonomous AI agent that supports bilingual (Arabic-English) students in understanding, improving, and producing academic work.

## 🌟 Features

- **Bilingual Academic Explanations**: Get complex concepts explained in both English and Arabic with Gulf-region examples
- **Academic Writing Improvement**: Submit your writing and get corrections with Arabic explanations
- **Autonomous Quiz Generation**: Automatically generated comprehension quizzes to test understanding
- **Personalized Learning Paths**: Get customized suggestions for next steps in your learning journey
- **Multi-Agent Architecture**: Demonstrates autonomous, multi-step agentic behavior

## 🏗️ Architecture

BABA uses a multi-agent architecture with autonomous decision-making:

```
User Input
    ↓
Orchestrator Agent
    ↓
Task Classifier Agent (Autonomous Decision Point 1)
    ↓
┌─────────────┴──────────────┐
↓                            ↓
Explainer Agent          Writer Agent
    ↓                        ↓
Quiz Agent              Feedback Agent
    ↓                        ↓
Feedback & Learning Path Suggestions
```

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Internet connection

## 🚀 Installation

### 1. Clone or Download the Project

```bash
cd A:\BABA
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Edit the `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_actual_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
```

**Important**: Replace `your_actual_openai_api_key_here` with your real OpenAI API key.

## 🎮 Usage

### Running Locally

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Using BABA

1. **For Concept Explanations**:
   - Type a question like: "What is critical thinking?"
   - Get bilingual explanations with Gulf-region examples
   - Take auto-generated quizzes to test understanding

2. **For Writing Improvement**:
   - Paste a paragraph of your academic writing
   - Get corrected text with Arabic explanations of changes
   - Learn grammar and style improvements

3. **View Autonomous Actions**:
   - Expand "Autonomous Agent Actions" to see BABA's decision-making process
   - Watch how agents coordinate to solve your task

## 📁 Project Structure

```
baba-project/
├── app.py                          # Main Streamlit application
├── config.py                       # Configuration management
├── requirements.txt                # Python dependencies
├── .env                           # Environment variables (API keys)
├── .env.example                   # Example environment file
├── .gitignore                     # Git ignore rules
│
├── agents/                        # Agent modules
│   ├── orchestrator.py            # Main orchestrator
│   ├── task_classifier.py         # Task classification
│   ├── explainer_agent.py         # Concept explanations
│   ├── writer_agent.py            # Writing improvement
│   ├── quiz_agent.py              # Quiz generation
│   └── feedback_agent.py          # Feedback & suggestions
│
├── prompts/                       # Prompt templates
│   ├── classifier_prompts.py      # Classification prompts
│   ├── explainer_prompts.py       # Explanation prompts
│   ├── writer_prompts.py          # Writing prompts
│   └── quiz_prompts.py            # Quiz prompts
│
└── utils/                         # Utility functions
    ├── llm_client.py              # OpenAI API wrapper
    ├── arabic_utils.py            # Arabic text processing
    └── validators.py              # Input validation
```

## 🔧 Configuration

### Environment Variables

Edit `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: Model to use (default: gpt-3.5-turbo)
- `APP_TITLE`: Application title
- `DEBUG_MODE`: Enable debug mode (True/False)

### Model Options

- `gpt-3.5-turbo`: Fast and cost-effective (recommended)
- `gpt-4`: More powerful but slower and more expensive
- `gpt-4-turbo`: Balance of speed and capability

## 🌐 Deployment

### Option 1: Streamlit Cloud (Free & Easy)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your `OPENAI_API_KEY` in Secrets:
   ```toml
   OPENAI_API_KEY = "your_key_here"
   ```
5. Deploy!

### Option 2: Railway

1. Install Railway CLI or use web interface
2. Connect GitHub repository
3. Add environment variables
4. Deploy

### Option 3: Render

1. Connect GitHub repository
2. Add environment variables
3. Deploy as Web Service

## 🧪 Testing Examples

### Example 1: Concept Explanation
**Input**: "What is critical thinking?"

**Expected Output**:
- English explanation
- Arabic translation
- Gulf-region example
- Auto-generated quiz
- Learning path suggestions

### Example 2: Writing Improvement
**Input**: "The research is show that climate change effect economy."

**Expected Output**:
- Corrected text: "The research shows that climate change affects the economy."
- Arabic explanation of changes
- Grammar points addressed
- Tone improvements

## 🤖 Autonomous Behavior

BABA demonstrates autonomous, multi-step behavior by:

1. **Automatic Task Classification**: Determines if you need explanation or writing help
2. **Context-Aware Actions**: Generates quizzes after explanations without being asked
3. **Intelligent Routing**: Directs your request to the appropriate specialized agent
4. **Proactive Feedback**: Suggests next steps based on your interaction
5. **Adaptive Responses**: Adjusts behavior based on session context

## 📊 Agent Responsibilities

| Agent | Responsibility | Autonomous Decisions |
|-------|---------------|---------------------|
| **Orchestrator** | Coordinates all agents | Routes tasks, triggers follow-ups |
| **Task Classifier** | Identifies user intent | Categorizes explanation vs writing |
| **Explainer** | Provides bilingual explanations | Adapts complexity to concept |
| **Writer** | Improves academic writing | Identifies key grammar/style issues |
| **Quiz Generator** | Creates comprehension tests | Designs questions testing understanding |
| **Feedback** | Analyzes performance | Suggests personalized learning paths |

## ⚠️ Troubleshooting

### API Key Error
```
Configuration Error: OPENAI_API_KEY not set!
```
**Solution**: Add your OpenAI API key to the `.env` file

### Module Not Found
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solution**: Run `pip install -r requirements.txt`

### JSON Parsing Error
**Solution**: The model sometimes returns invalid JSON. The system has fallback mechanisms, but you may need to retry.

### Arabic Text Not Displaying Correctly
**Solution**: Ensure your browser supports Arabic fonts. Most modern browsers do by default.

## 💰 Cost Estimation

Using `gpt-3.5-turbo`:
- Explanation request: ~$0.002-0.005
- Writing improvement: ~$0.003-0.008
- Quiz generation: ~$0.002-0.004

**Estimated cost per session**: $0.01-0.02

## 🔐 Security Notes

- Never commit `.env` file to version control
- Keep your API keys private
- Use environment variables for sensitive data
- The `.gitignore` file is configured to protect secrets

## 🎯 Project Goals

This project demonstrates:
1. ✅ Autonomous AI agent behavior
2. ✅ Multi-agent coordination
3. ✅ Bilingual academic support
4. ✅ Context-aware decision making
5. ✅ Pedagogical value for students

## 📝 License

This project was created for educational purposes as part of the BABA development brief.

## 👥 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the example interactions
3. Ensure your API key is valid and has credits

## 🚦 Next Steps

After setup:
1. ✅ Add your OpenAI API key to `.env`
2. ✅ Install dependencies
3. ✅ Run the application
4. ✅ Try example interactions
5. ✅ Deploy to Streamlit Cloud (optional)

---

**Built with**: Python | Streamlit | OpenAI GPT | Claude Code

**Version**: 1.0.0

**Date**: 2025
