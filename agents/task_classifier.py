"""
Task Classifier Agent.

Classifies user input into task types (explanation or writing improvement).
"""

from typing import Dict, Any
from utils.llm_client import llm_client
from utils.validators import validators
from prompts.classifier_prompts import (
    CLASSIFIER_SYSTEM_PROMPT,
    CLASSIFIER_USER_PROMPT_TEMPLATE
)


class TaskClassifierAgent:
    """Agent responsible for classifying user input into task types."""

    def __init__(self):
        """Initialize the task classifier agent."""
        self.name = "Task Classifier"

    def classify(self, user_input: str) -> Dict[str, Any]:
        """
        Classify user input into a task type.

        Args:
            user_input: The user's input text

        Returns:
            Dictionary containing:
                - task_type: "explanation" or "writing_improvement"
                - confidence: float between 0 and 1
                - detected_language: "ar", "en", or "mixed"
                - reasoning: explanation of the classification

        Raises:
            Exception: If classification fails
        """
        try:
            # Format the user prompt
            user_prompt = CLASSIFIER_USER_PROMPT_TEMPLATE.format(
                user_input=user_input
            )

            # Call LLM for classification
            result = llm_client.generate_json_completion(
                system_prompt=CLASSIFIER_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                temperature=0.3  # Lower temperature for more consistent classification
            )

            # Validate the result
            is_valid, error_msg = validators.validate_task_classification(result)
            if not is_valid:
                raise ValueError(f"Invalid classification result: {error_msg}")

            return result

        except Exception as e:
            # Fallback classification based on simple heuristics
            return self._fallback_classification(user_input, str(e))

    def _fallback_classification(self, user_input: str, error: str) -> Dict[str, Any]:
        """
        Provide a fallback classification when LLM fails.

        Args:
            user_input: The user's input text
            error: Error message from the failed LLM call

        Returns:
            Basic classification result
        """
        user_input_lower = user_input.lower().strip()

        # Check for quiz-related keywords first (highest priority)
        quiz_indicators = [
            "quiz", "test", "exam", "اختبار", "امتحان",
            "yes", "yeah", "ok", "sure", "نعم", "أجل", "موافق"
        ]
        is_quiz = any(indicator in user_input_lower for indicator in quiz_indicators)

        # Very short affirmative responses are likely quiz requests
        if user_input_lower in ["yes", "yeah", "ok", "sure", "y", "نعم", "أجل", "موافق"]:
            is_quiz = True

        # Check for explanation indicators (academic concepts)
        explanation_indicators = ["what is", "what are", "explain the concept", "define", "ما هو", "ما هي"]
        is_academic_question = any(indicator in user_input_lower for indicator in explanation_indicators)

        # Check for general question indicators
        general_indicators = ["how to", "how can", "how do", "advice", "help me", "hello", "hi", "thanks",
                             "كيف", "نصيحة", "مرحبا", "شكرا"]
        is_general = any(indicator in user_input_lower for indicator in general_indicators)

        # Check for greeting keywords
        greeting_indicators = ["hello", "hi", "hey", "good morning", "good evening", "مرحبا", "السلام"]
        is_greeting = any(indicator in user_input_lower for indicator in greeting_indicators)

        # Check length - longer texts are more likely to be writing samples
        is_long = len(user_input.split()) > 20

        # Classification priority: quiz > greeting > academic concept > long text > general question
        if is_quiz:
            task_type = "quiz_generation"
        elif is_greeting:
            task_type = "general_question"
        elif is_academic_question and not is_long:
            task_type = "explanation"
        elif is_long:
            task_type = "writing_improvement"
        elif is_general:
            task_type = "general_question"
        else:
            # Default to general question for unclear inputs
            task_type = "general_question"

        return {
            "task_type": task_type,
            "confidence": 0.6,  # Lower confidence for fallback
            "detected_language": "unknown",
            "reasoning": f"Fallback classification due to error: {error}"
        }


# Global instance
task_classifier = TaskClassifierAgent()
