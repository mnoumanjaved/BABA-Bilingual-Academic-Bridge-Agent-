"""
Orchestrator Agent.

Coordinates all other agents and implements autonomous multi-step behavior.
"""

from typing import Dict, Any, Optional
from utils.validators import validators
from agents.task_classifier import task_classifier
from agents.explainer_agent import explainer_agent
from agents.writer_agent import writer_agent
from agents.quiz_agent import quiz_agent
from agents.feedback_agent import feedback_agent


class OrchestratorAgent:
    """Main orchestrator that coordinates all sub-agents."""

    def __init__(self):
        """Initialize the orchestrator."""
        self.name = "BABA Orchestrator"
        self.current_state = {}

    def process_user_input(
        self,
        user_input: str,
        session_state: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Process user input through the autonomous agent pipeline.

        This is the main entry point that demonstrates autonomous behavior by:
        1. Classifying the task
        2. Routing to appropriate agent
        3. Generating follow-up actions autonomously
        4. Providing learning path suggestions

        Args:
            user_input: The user's input text
            session_state: Optional session state for context

        Returns:
            Dictionary with complete processing results including:
                - classification: Task classification results
                - main_result: Main agent output
                - autonomous_actions: List of autonomous follow-up actions taken
                - suggested_next_steps: Learning path suggestions
                - error: Error message if any
        """
        result = {
            "classification": None,
            "main_result": None,
            "autonomous_actions": [],
            "suggested_next_steps": None,
            "error": None
        }

        try:
            # Step 1: Validate input
            is_valid, error_msg = validators.validate_user_input(user_input)
            if not is_valid:
                result["error"] = error_msg
                return result

            # Step 2: Classify the task (Autonomous Decision Point 1)
            classification = task_classifier.classify(user_input)
            result["classification"] = classification
            result["autonomous_actions"].append({
                "agent": "Task Classifier",
                "action": "Classified input",
                "decision": f"Determined task type: {classification['task_type']}"
            })

            # Step 3: Route to appropriate agent based on classification
            task_type = classification["task_type"]

            if task_type == "explanation":
                # Handle explanation flow
                result.update(self._handle_explanation_flow(user_input, session_state))

            elif task_type == "writing_improvement":
                # Handle writing improvement flow
                result.update(self._handle_writing_flow(user_input, session_state))

            elif task_type == "quiz_generation":
                # Handle quiz generation flow
                result.update(self._handle_quiz_generation_flow(user_input, session_state))

            else:
                result["error"] = f"Unknown task type: {task_type}"

        except Exception as e:
            result["error"] = f"Processing error: {str(e)}"

        return result

    def _handle_explanation_flow(
        self,
        user_input: str,
        session_state: Optional[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Handle the explanation workflow with autonomous actions.

        Args:
            user_input: The concept to explain
            session_state: Session state

        Returns:
            Dictionary with explanation results and autonomous actions
        """
        result = {
            "main_result": None,
            "autonomous_actions": [],
            "suggested_next_steps": None
        }

        try:
            # Get explanation from explainer agent
            explanation = explainer_agent.explain(user_input)
            result["main_result"] = {
                "type": "explanation",
                "data": explanation
            }
            result["autonomous_actions"].append({
                "agent": "Explainer",
                "action": "Generated bilingual explanation",
                "decision": "Provided academic explanation with Gulf-region example"
            })

            # Store explanation content in session for potential quiz generation
            if session_state is not None:
                session_state["last_explanation"] = explanation
                session_state["last_topic"] = user_input

            # Autonomous Decision Point 2: Suggest quiz (don't auto-generate)
            # Add a prompt asking if user wants a quiz
            result["quiz_prompt"] = {
                "message_en": "Would you like to test your understanding with a quiz on this topic?",
                "message_ar": "هل تريد اختبار فهمك من خلال اختبار حول هذا الموضوع؟"
            }
            result["autonomous_actions"].append({
                "agent": "Orchestrator",
                "action": "Suggested quiz option",
                "decision": "Offered quiz to test comprehension (user choice)"
            })

            # Removed suggested next steps - keeping interface clean and conversational
            # Users can continue the conversation naturally instead

        except Exception as e:
            result["error"] = f"Explanation flow error: {str(e)}"

        return result

    def _handle_writing_flow(
        self,
        user_input: str,
        session_state: Optional[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Handle the writing improvement workflow with autonomous actions.

        Args:
            user_input: The text to improve
            session_state: Session state

        Returns:
            Dictionary with writing results and autonomous actions
        """
        result = {
            "main_result": None,
            "autonomous_actions": [],
            "suggested_next_steps": None
        }

        try:
            # Get improved writing from writer agent
            improved = writer_agent.improve(user_input)
            result["main_result"] = {
                "type": "writing_improvement",
                "data": improved
            }
            result["autonomous_actions"].append({
                "agent": "Writer",
                "action": "Improved academic writing",
                "decision": "Rewrote text with formal academic style"
            })

            # Store writing content in session for potential quiz generation
            if session_state is not None:
                session_state["last_writing"] = improved
                session_state["last_topic"] = "writing improvement"

            # Autonomous Decision Point 2: Analyze feedback
            result["autonomous_actions"].append({
                "agent": "Feedback",
                "action": "Analyzed writing improvements",
                "decision": f"Identified {len(improved.get('grammar_points', []))} grammar points"
            })

            # Suggest quiz on writing skills (don't auto-generate)
            result["quiz_prompt"] = {
                "message_en": "Would you like a quiz to practice similar writing skills?",
                "message_ar": "هل تريد اختبارًا لممارسة مهارات الكتابة المماثلة؟"
            }

            # Removed suggested next steps - keeping interface clean and conversational
            # Users can continue the conversation naturally instead

        except Exception as e:
            result["error"] = f"Writing flow error: {str(e)}"

        return result

    def _handle_quiz_generation_flow(
        self,
        user_input: str,
        session_state: Optional[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Handle quiz generation when user explicitly requests it.

        Args:
            user_input: The user's quiz request
            session_state: Session state with context

        Returns:
            Dictionary with quiz results
        """
        result = {
            "main_result": None,
            "autonomous_actions": [],
            "suggested_next_steps": None
        }

        try:
            # Check if user is just affirming (yes, ok, sure) - use previous context
            # Also include standalone words like "quiz", "test", "exam" as affirmative
            affirmative_responses = ["yes", "yeah", "ok", "sure", "y", "quiz", "test", "exam",
                                    "نعم", "أجل", "موافق", "اختبار", "امتحان"]
            is_simple_affirmation = user_input.lower().strip() in affirmative_responses

            # Check if user is explicitly specifying a quiz topic (not just affirming)
            quiz_topic_keywords = ["quiz on", "quiz about", "test on", "test about",
                                  "generate quiz", "create quiz", "make quiz",
                                  "اختبار عن", "اختبار حول"]
            has_explicit_topic = any(keyword in user_input.lower() for keyword in quiz_topic_keywords)

            if is_simple_affirmation and not has_explicit_topic:
                # User is responding to a quiz suggestion - use previous context
                if session_state and "last_explanation" in session_state:
                    # Generate quiz based on previous explanation
                    explanation = session_state["last_explanation"]
                    quiz_content = f"{explanation.get('english_explanation', '')}\n\n{explanation.get('gulf_example', '')}"

                    quiz = quiz_agent.generate(quiz_content)
                    result["main_result"] = {
                        "type": "quiz",
                        "data": quiz
                    }
                    result["autonomous_actions"].append({
                        "agent": "Quiz Generator",
                        "action": "Generated comprehension quiz",
                        "decision": "Created bilingual quiz based on previous explanation"
                    })

                elif session_state and "last_writing" in session_state and not has_explicit_topic:
                    # Generate quiz on writing skills (only if no explicit topic specified)
                    writing = session_state["last_writing"]
                    quiz_content = f"Writing skills quiz based on: {writing.get('improved_text', '')}"

                    quiz = quiz_agent.generate(quiz_content)
                    result["main_result"] = {
                        "type": "quiz",
                        "data": quiz
                    }
                    result["autonomous_actions"].append({
                        "agent": "Quiz Generator",
                        "action": "Generated writing skills quiz",
                        "decision": "Created quiz to practice writing concepts"
                    })

                else:
                    # No context - ask for topic
                    result["main_result"] = {
                        "type": "message",
                        "data": {
                            "message_en": "I'd be happy to create a quiz for you! What topic would you like to be tested on?",
                            "message_ar": "يسعدني إنشاء اختبار لك! ما الموضوع الذي تريد أن تُختبر عليه؟"
                        }
                    }

            else:
                # User specified a topic or asked for quiz on something specific
                # Extract the topic from user input
                topic = self._extract_quiz_topic(user_input)

                # First get explanation of the topic (always generate fresh content)
                explanation = explainer_agent.explain(topic)

                # Store for potential future reference
                if session_state is not None:
                    session_state["last_explanation"] = explanation
                    session_state["last_topic"] = topic

                # Generate quiz based on the NEW explanation
                quiz_content = f"{explanation.get('english_explanation', '')}\n\n{explanation.get('gulf_example', '')}"
                quiz = quiz_agent.generate(quiz_content)

                result["main_result"] = {
                    "type": "quiz",
                    "data": quiz
                }
                result["autonomous_actions"].append({
                    "agent": "Explainer",
                    "action": "Generated fresh content for quiz",
                    "decision": f"Created new explanation about '{topic}' as basis for quiz"
                })
                result["autonomous_actions"].append({
                    "agent": "Quiz Generator",
                    "action": "Generated quiz on specified topic",
                    "decision": f"Created bilingual quiz on '{topic}' using fresh content"
                })

        except Exception as e:
            result["error"] = f"Quiz generation error: {str(e)}"

        return result

    def _extract_quiz_topic(self, user_input: str) -> str:
        """
        Extract the quiz topic from user input.

        Args:
            user_input: The user's input

        Returns:
            The extracted topic
        """
        import re

        # Remove common quiz keywords to extract the topic (order matters - longer phrases first)
        quiz_keywords = [
            "generate a quiz on the topic",
            "generate quiz on the topic",
            "create a quiz on the topic",
            "create quiz on the topic",
            "make a quiz on the topic",
            "make quiz on the topic",
            "quiz on the topic",
            "test on the topic",
            "generate a quiz on",
            "generate quiz on",
            "create a quiz on",
            "create quiz on",
            "make a quiz on",
            "make quiz on",
            "quiz on",
            "quiz about",
            "test on",
            "test about",
            "generate quiz",
            "create quiz",
            "make quiz",
            "اختبار عن",
            "اختبار حول",
        ]

        topic = user_input.lower()

        # Remove quiz keywords (longest first to avoid partial matches)
        for keyword in quiz_keywords:
            topic = topic.replace(keyword, " ")

        # Clean up whitespace first
        topic = " ".join(topic.split()).strip()

        # Check if it's a "what is X" or "how does X" type question
        # If so, preserve it as-is for better context
        question_patterns = [
            r'what is \w+',
            r'what are \w+',
            r'how does \w+',
            r'how do \w+',
            r'why is \w+',
            r'why are \w+',
            r'explain \w+'
        ]

        is_question_format = any(re.search(pattern, topic) for pattern in question_patterns)

        if not is_question_format:
            # Only remove common words if it's NOT a question format
            # This preserves question context like "what is langgraph"
            words_to_remove = ["generate", "create", "make", "quiz", "test", "exam", "the", "a", "an"]
            for word in words_to_remove:
                # Use regex to match whole words only
                topic = re.sub(r'\b' + re.escape(word) + r'\b', '', topic)

        # Remove punctuation
        topic = topic.replace("?", "").replace("!", "").replace(",", "")

        # Clean up whitespace again
        topic = " ".join(topic.split()).strip()

        # If topic is still empty or too short, use original input
        if len(topic) < 3:
            topic = user_input

        return topic

    def check_quiz_answer(
        self,
        question_index: int,
        user_answer: int,
        quiz_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Check a quiz answer and provide feedback.

        Args:
            question_index: Index of the question
            user_answer: User's selected answer index
            quiz_data: The quiz data

        Returns:
            Dictionary with answer check results and feedback
        """
        # Check the answer
        answer_result = quiz_agent.check_answer(question_index, user_answer, quiz_data)

        # Provide encouragement based on correctness
        if answer_result["is_correct"]:
            encouragement = feedback_agent.generate_encouragement("excellent")
        else:
            encouragement = feedback_agent.generate_encouragement("needs_improvement")

        return {
            **answer_result,
            "encouragement": encouragement
        }

    def analyze_session_performance(
        self,
        session_state: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Analyze overall session performance.

        Args:
            session_state: Complete session state with quiz history

        Returns:
            Performance analysis and recommendations
        """
        quiz_history = session_state.get("quiz_history", [])

        if not quiz_history:
            return {
                "message": "No quiz attempts yet. Try taking a quiz to test your understanding!",
                "message_ar": "لم تجرب أي اختبار بعد. حاول أخذ اختبار لاختبار فهمك!"
            }

        total_questions = len(quiz_history)
        correct_answers = sum(1 for q in quiz_history if q.get("is_correct", False))

        analysis = feedback_agent.analyze_quiz_performance(total_questions, correct_answers)

        return analysis


# Global instance
orchestrator = OrchestratorAgent()
