"""
BABA - Bilingual Academic Bridge Agent
Main Streamlit Application

An autonomous AI agent that supports bilingual (Arabic-English) students
in understanding, improving, and producing academic work.
"""

import streamlit as st
from config import config
from agents.orchestrator import orchestrator
from utils.arabic_utils import arabic_utils

# Page configuration
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.PAGE_ICON,
    layout=config.LAYOUT,
    initial_sidebar_state="expanded"
)

# Custom CSS for ChatGPT-like interface
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 48rem;
    }

    /* ChatGPT-style message styling */
    .stChatMessage {
        padding: 1.5rem 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }

    /* User message styling */
    [data-testid="stChatMessageContent"] {
        background-color: transparent;
    }

    /* Arabic text support */
    .arabic-text {
        direction: rtl;
        text-align: right;
        font-family: 'Traditional Arabic', 'Arial', sans-serif;
        font-size: 1.05em;
        line-height: 1.8;
    }

    .english-text {
        direction: ltr;
        text-align: left;
        line-height: 1.6;
    }

    /* Bilingual container for side-by-side display */
    .bilingual-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin: 1rem 0;
    }

    .bilingual-column {
        padding: 1rem;
        background-color: rgba(0, 0, 0, 0.02);
        border-radius: 0.5rem;
        border: 1px solid rgba(0, 0, 0, 0.1);
    }

    /* Section headers */
    .section-header {
        font-size: 1.1em;
        font-weight: 600;
        margin-bottom: 0.5rem;
        color: #2c3e50;
    }

    /* Info boxes */
    .info-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #0ea5e9;
        margin: 0.5rem 0;
    }

    .success-box {
        background-color: #e7f9f0;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #10b981;
        margin: 0.5rem 0;
    }

    .agent-action {
        background-color: #f8f9fa;
        padding: 0.75rem;
        border-radius: 0.375rem;
        margin: 0.5rem 0;
        border-left: 3px solid #6366f1;
        font-size: 0.9em;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }

    ::-webkit-scrollbar-thumb {
        background: #888;
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #555;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = None

    if "quiz_history" not in st.session_state:
        st.session_state.quiz_history = []

    if "current_result" not in st.session_state:
        st.session_state.current_result = None

    if "interaction_count" not in st.session_state:
        st.session_state.interaction_count = 0


def render_header():
    """Render the application header."""
    st.markdown(f"""
    <div style='text-align: center; padding: 1rem 0; border-bottom: 1px solid rgba(0,0,0,0.1);'>
        <h1 style='margin: 0; font-size: 1.5rem;'>{config.PAGE_ICON} BABA</h1>
        <p style='margin: 0.25rem 0 0 0; font-size: 0.9rem; color: #666;'>
            Bilingual Academic Bridge Agent | وكيل الجسر الأكاديمي ثنائي اللغة
        </p>
    </div>
    """, unsafe_allow_html=True)


def render_sidebar():
    """Render the sidebar with information and settings."""
    with st.sidebar:
        st.header("About BABA")
        st.markdown("""
        BABA is an autonomous AI agent designed to help bilingual Arabic-English students with:

        - 📚 Understanding academic concepts
        - ✍️ Improving academic writing
        - 🎯 Testing comprehension through quizzes
        - 🌟 Personalized learning paths

        **How it works:**
        1. Enter your question or text
        2. BABA autonomously determines what you need
        3. Get bilingual explanations or writing feedback
        4. Test your knowledge with auto-generated quizzes
        """)

        st.markdown("---")

        st.header("Examples")
        st.markdown("""
        **For Explanations:**
        - "What is critical thinking?"
        - "Explain the concept of sustainability"

        **For Writing Help:**
        - Paste a paragraph you've written
        - Get corrections and Arabic explanations
        """)

        st.markdown("---")

        # Session statistics
        if st.session_state.interaction_count > 0:
            st.header("Session Stats")
            st.metric("Interactions", st.session_state.interaction_count)

            if st.session_state.quiz_history:
                correct = sum(1 for q in st.session_state.quiz_history if q.get("is_correct", False))
                total = len(st.session_state.quiz_history)
                st.metric("Quiz Score", f"{correct}/{total}")

        st.markdown("---")

        if st.button("🔄 Clear Session", use_container_width=True):
            st.session_state.clear()
            st.rerun()


def display_autonomous_actions(actions):
    """Display the autonomous actions taken by the system."""
    if not actions:
        return

    with st.expander("🤖 Autonomous Agent Actions (See How BABA Thinks)", expanded=False):
        st.markdown("### Agent Decision-Making Process")
        for i, action in enumerate(actions, 1):
            st.markdown(f"""
            <div class="agent-action">
                <strong>Step {i}: {action['agent']}</strong><br/>
                <em>Action:</em> {action['action']}<br/>
                <em>Decision:</em> {action['decision']}
            </div>
            """, unsafe_allow_html=True)


def display_explanation_result(data):
    """Display explanation results in bilingual format."""
    st.markdown("**📚 Academic Explanation | الشرح الأكاديمي**")
    st.markdown("")

    # Bilingual explanation side by side
    st.markdown(f"""
    <div class="bilingual-container">
        <div class="bilingual-column">
            <div class="section-header">English Explanation</div>
            <div class="english-text">{data["english_explanation"]}</div>
        </div>
        <div class="bilingual-column">
            <div class="section-header">الشرح بالعربية</div>
            <div class="arabic-text">{data["arabic_explanation"]}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Gulf example
    if data.get("gulf_example"):
        st.markdown("")
        st.markdown("**🌍 Gulf Region Example | مثال من منطقة الخليج**")
        st.markdown(f'<div class="info-box">{data["gulf_example"]}</div>', unsafe_allow_html=True)

    # Key terms
    if data.get("key_terms"):
        st.markdown("")
        st.markdown(f"**🔑 Key Terms:** {', '.join(data['key_terms'])}")


def display_writing_result(data):
    """Display writing improvement results."""
    st.markdown("**✍️ Writing Improvement | تحسين الكتابة**")
    st.markdown("")

    # Check if input was in Arabic or English
    input_language = data.get("input_language", "en")

    if input_language == "ar":
        # For Arabic input: Show improved Arabic + English translation
        st.markdown("**Improved Academic Text (Arabic):**")
        st.markdown(f'<div class="success-box arabic-text">{data["improved_text"]}</div>',
                   unsafe_allow_html=True)

        # English translation of improved text
        if data.get("english_translation"):
            st.markdown("")
            st.markdown("**English Translation of Improved Text:**")
            st.markdown(f'<div class="info-box english-text">{data["english_translation"]}</div>',
                       unsafe_allow_html=True)

        # Changes explanation in Arabic
        st.markdown("")
        st.markdown("**شرح التغييرات (Changes Explanation):**")
        st.markdown(f'<div class="info-box arabic-text">{data["changes_explanation_ar"]}</div>',
                   unsafe_allow_html=True)

    else:
        # For English input: Show improved English + Arabic translation
        st.markdown("**Improved Academic Text (English):**")
        st.markdown(f'<div class="success-box english-text">{data["improved_text"]}</div>',
                   unsafe_allow_html=True)

        # Arabic translation of improved text
        if data.get("arabic_translation"):
            st.markdown("")
            st.markdown("**Arabic Translation of Improved Text:**")
            st.markdown(f'<div class="info-box arabic-text">{data["arabic_translation"]}</div>',
                       unsafe_allow_html=True)

        # Changes explanation in Arabic
        st.markdown("")
        st.markdown("**شرح التغييرات (Changes Explained in Arabic):**")
        st.markdown(f'<div class="info-box arabic-text">{data["changes_explanation_ar"]}</div>',
                   unsafe_allow_html=True)

    # Grammar points
    if data.get("grammar_points") and len(data["grammar_points"]) > 0:
        st.markdown("")
        st.markdown("**📝 Grammar Points Addressed:**")
        for point in data["grammar_points"]:
            st.markdown(f"• {point}")

    # Tone improvements
    if data.get("tone_improvements") and len(data["tone_improvements"]) > 0:
        st.markdown("")
        st.markdown("**🎨 Tone & Style Improvements:**")
        for improvement in data["tone_improvements"]:
            st.markdown(f"• {improvement}")


def display_quiz(quiz_data, quiz_id=None):
    """Display quiz questions."""
    if not quiz_data or "questions" not in quiz_data:
        return

    # Generate unique quiz ID if not provided
    if quiz_id is None:
        import time
        quiz_id = int(time.time() * 1000)

    st.markdown("---")
    st.markdown("### 🎯 Test Your Understanding | اختبر فهمك")

    questions = quiz_data["questions"]

    for i, question in enumerate(questions):
        st.markdown(f"#### Question {i+1}")

        # Display question in both languages
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**{question['question_en']}**")
        with col2:
            st.markdown(f'<div class="arabic-text"><strong>{question["question_ar"]}</strong></div>',
                       unsafe_allow_html=True)

        # Get options (use Arabic if available, otherwise English)
        options = question.get("options_ar", question["options"])

        # Radio buttons for answers with unique key
        user_answer = st.radio(
            f"Select your answer:",
            options=range(len(options)),
            format_func=lambda x: options[x],
            key=f"quiz_q_{i}_{quiz_id}"
        )

        # Check answer button with unique key
        if st.button(f"Check Answer", key=f"check_{i}_{quiz_id}"):
            result = orchestrator.check_quiz_answer(i, user_answer, quiz_data)

            # Store in history
            st.session_state.quiz_history.append({
                "question_index": i,
                "user_answer": user_answer,
                "is_correct": result["is_correct"]
            })

            # Display result
            if result["is_correct"]:
                st.success(f"✅ {result['explanation']}")
                st.balloons()
            else:
                st.error(f"❌ {result['explanation']}")

            st.info(result["encouragement"])


def display_next_steps(next_steps):
    """Display suggested next steps."""
    if not next_steps:
        return

    st.markdown("**🚀 Suggested Next Steps | الخطوات التالية المقترحة**")
    st.markdown("")

    # Display in bilingual columns
    st.markdown("""
    <div class="bilingual-container">
        <div class="bilingual-column">
            <div class="section-header">English</div>
    """, unsafe_allow_html=True)

    for step in next_steps.get("next_steps", []):
        st.markdown(f"• {step}")

    st.markdown("""
        </div>
        <div class="bilingual-column">
            <div class="section-header">العربية</div>
            <div class="arabic-text">
    """, unsafe_allow_html=True)

    for step in next_steps.get("next_steps_ar", []):
        st.markdown(f"• {step}")

    st.markdown("""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def main():
    """Main application function."""
    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        st.error(f"⚠️ Configuration Error: {str(e)}")
        st.info("Please add your OpenAI API key to the .env file")
        st.stop()

    # Initialize session state
    initialize_session_state()

    # Render UI components
    render_header()
    render_sidebar()

    # Display welcome message if no messages yet
    if len(st.session_state.messages) == 0:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown("""
            Welcome to **BABA** - Your Bilingual Academic Bridge Agent!

            I can help you with:
            • 📚 **Understanding** academic concepts (in English & Arabic)
            • ✍️ **Improving** your academic writing
            • 🎯 **Testing** your knowledge with quizzes

            Just type your question or paste text you'd like me to review!
            """)

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message.get("avatar", None)):
            if message["role"] == "user":
                st.markdown(message["content"])
            else:
                # Display assistant response with all components
                if "result" in message:
                    result = message["result"]

                    # Show classification
                    if result.get("classification"):
                        classification = result["classification"]
                        st.caption(f"✅ Task: **{classification['task_type'].replace('_', ' ').title()}** (Confidence: {classification['confidence']:.0%})")

                    # Show autonomous actions in expander
                    if result.get("autonomous_actions"):
                        with st.expander("🤖 See How BABA Thinks", expanded=False):
                            for i, action in enumerate(result["autonomous_actions"], 1):
                                st.markdown(f"""
                                <div class="agent-action">
                                    <strong>Step {i}: {action['agent']}</strong><br/>
                                    <em>{action['action']}</em> - {action['decision']}
                                </div>
                                """, unsafe_allow_html=True)

                    # Display main result
                    if result.get("main_result"):
                        main_result = result["main_result"]

                        if main_result["type"] == "explanation":
                            display_explanation_result(main_result["data"])

                        elif main_result["type"] == "writing_improvement":
                            display_writing_result(main_result["data"])

                        elif main_result["type"] == "quiz":
                            st.markdown("**🎯 Quiz Time! | وقت الاختبار!**")
                            st.markdown("")
                            # Use quiz_id from message if available
                            quiz_id = message.get("quiz_id")
                            display_quiz(main_result["data"], quiz_id)

                        elif main_result["type"] == "message":
                            # Display bilingual message
                            msg_data = main_result["data"]
                            st.markdown(f"**{msg_data.get('message_en', '')}**")
                            st.markdown(f"**{msg_data.get('message_ar', '')}**")

                    # Display quiz prompt (suggestion to take quiz)
                    if result.get("quiz_prompt"):
                        st.markdown("")
                        st.markdown("---")
                        quiz_prompt = result["quiz_prompt"]
                        st.info(f"💡 {quiz_prompt['message_en']}\n\n{quiz_prompt['message_ar']}\n\n*Type 'yes' or 'quiz' to generate a quiz!*")

                    # Display next steps
                    if result.get("suggested_next_steps"):
                        st.markdown("")
                        st.markdown("---")
                        display_next_steps(result["suggested_next_steps"])

                elif "error" in message:
                    st.error(f"❌ {message['error']}")
                else:
                    st.markdown(message.get("content", ""))

    # Chat input at the bottom (ChatGPT style)
    user_input = st.chat_input("Message BABA... (Type in English or Arabic)", key="chat_input")

    # Process user input
    if user_input:
        # Add user message to chat
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "avatar": "👤"
        })

        # Display user message immediately
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)

        # Process through orchestrator
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("Thinking..."):
                result = orchestrator.process_user_input(user_input, st.session_state)

                # Increment interaction count
                st.session_state.interaction_count += 1

            # Display results
            if result.get("error"):
                st.error(f"❌ Error: {result['error']}")
                st.session_state.messages.append({
                    "role": "assistant",
                    "error": result['error'],
                    "avatar": "🤖"
                })
            else:
                # Show classification
                if result.get("classification"):
                    classification = result["classification"]
                    st.caption(f"✅ Task: **{classification['task_type'].replace('_', ' ').title()}** (Confidence: {classification['confidence']:.0%})")

                # Show autonomous actions
                if result.get("autonomous_actions"):
                    with st.expander("🤖 See How BABA Thinks", expanded=False):
                        for i, action in enumerate(result["autonomous_actions"], 1):
                            st.markdown(f"""
                            <div class="agent-action">
                                <strong>Step {i}: {action['agent']}</strong><br/>
                                <em>{action['action']}</em> - {action['decision']}
                            </div>
                            """, unsafe_allow_html=True)

                # Display main result
                if result.get("main_result"):
                    main_result = result["main_result"]

                    if main_result["type"] == "explanation":
                        display_explanation_result(main_result["data"])

                        # Display quiz if generated (legacy - should not happen anymore)
                        if "quiz" in main_result:
                            st.markdown("")
                            st.markdown("---")
                            import time
                            quiz_id_legacy = int(time.time() * 1000)
                            display_quiz(main_result["quiz"], quiz_id_legacy)

                    elif main_result["type"] == "writing_improvement":
                        display_writing_result(main_result["data"])

                    elif main_result["type"] == "quiz":
                        st.markdown("**🎯 Quiz Time! | وقت الاختبار!**")
                        st.markdown("")
                        # Generate unique quiz ID for new quiz
                        import time
                        quiz_id = int(time.time() * 1000)
                        display_quiz(main_result["data"], quiz_id)

                    elif main_result["type"] == "message":
                        # Display bilingual message
                        msg_data = main_result["data"]
                        st.markdown(f"**{msg_data.get('message_en', '')}**")
                        st.markdown(f"**{msg_data.get('message_ar', '')}**")

                # Display quiz prompt (suggestion to take quiz)
                if result.get("quiz_prompt"):
                    st.markdown("")
                    st.markdown("---")
                    quiz_prompt = result["quiz_prompt"]
                    st.info(f"💡 {quiz_prompt['message_en']}\n\n{quiz_prompt['message_ar']}\n\n*Type 'yes' or 'quiz' to generate a quiz!*")

                # Display next steps
                if result.get("suggested_next_steps"):
                    st.markdown("")
                    st.markdown("---")
                    display_next_steps(result["suggested_next_steps"])

                # Store assistant response with quiz_id if it's a quiz
                message_data = {
                    "role": "assistant",
                    "result": result,
                    "avatar": "🤖"
                }

                # Add quiz_id if this is a quiz result
                if result.get("main_result") and result["main_result"].get("type") == "quiz":
                    import time
                    message_data["quiz_id"] = int(time.time() * 1000)

                st.session_state.messages.append(message_data)

        # Rerun to update chat display
        st.rerun()


if __name__ == "__main__":
    main()
