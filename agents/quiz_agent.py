"""
Quiz Agent.

Generates bilingual comprehension quizzes.
"""

from typing import Dict, Any
from utils.llm_client import llm_client
from utils.validators import validators
from prompts.quiz_prompts import (
    QUIZ_SYSTEM_PROMPT,
    QUIZ_USER_PROMPT_TEMPLATE
)


class QuizAgent:
    """Agent responsible for generating bilingual quizzes."""

    def __init__(self):
        """Initialize the quiz agent."""
        self.name = "Quiz Generator"

    def generate(self, explanation_content: str) -> Dict[str, Any]:
        """
        Generate a bilingual quiz based on an explanation.

        Args:
            explanation_content: The explanation to base the quiz on

        Returns:
            Dictionary containing:
                - questions: List of question dictionaries, each with:
                    - question_en: Question in English
                    - question_ar: Question in Arabic
                    - options: List of options
                    - options_ar: List of options in Arabic
                    - correct_answer: Index of correct option
                    - explanation: Why the answer is correct

        Raises:
            Exception: If quiz generation fails
        """
        try:
            # Format the user prompt
            user_prompt = QUIZ_USER_PROMPT_TEMPLATE.format(
                explanation_content=explanation_content
            )

            # Call LLM for quiz generation
            result = llm_client.generate_json_completion(
                system_prompt=QUIZ_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                temperature=0.7,
                max_tokens=1500
            )

            # Validate the result
            is_valid, error_msg = validators.validate_quiz_result(result)
            if not is_valid:
                raise ValueError(f"Invalid quiz result: {error_msg}")

            return result

        except Exception as e:
            raise Exception(f"Quiz agent failed: {str(e)}")

    def check_answer(
        self,
        question_index: int,
        user_answer: int,
        quiz_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Check if a user's answer is correct.

        Args:
            question_index: Index of the question being answered
            user_answer: Index of the option selected by user
            quiz_data: The quiz data containing questions

        Returns:
            Dictionary with:
                - is_correct: Boolean
                - explanation: Explanation of why the answer is correct/incorrect
        """
        if question_index >= len(quiz_data["questions"]):
            return {
                "is_correct": False,
                "explanation": "Invalid question index"
            }

        question = quiz_data["questions"][question_index]
        correct_answer = question["correct_answer"]
        is_correct = (user_answer == correct_answer)

        explanation = question.get("explanation", "No explanation provided.")

        if is_correct:
            message = f"Correct! {explanation}"
        else:
            correct_option = question["options"][correct_answer]
            message = f"Incorrect. The correct answer is: {correct_option}. {explanation}"

        return {
            "is_correct": is_correct,
            "explanation": message
        }


# Global instance
quiz_agent = QuizAgent()
