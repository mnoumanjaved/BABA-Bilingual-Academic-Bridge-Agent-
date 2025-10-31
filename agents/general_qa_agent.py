"""
General Q&A Agent.

Handles general questions that don't fit into explanation, writing improvement, or quiz categories.
Provides bilingual responses to diverse questions.
"""

from typing import Dict, Any
from utils.llm_client import llm_client
from utils.validators import validators
from prompts.general_qa_prompts import (
    GENERAL_QA_SYSTEM_PROMPT,
    GENERAL_QA_USER_PROMPT_TEMPLATE
)


class GeneralQAAgent:
    """Agent responsible for answering general questions bilingually."""

    def __init__(self):
        """Initialize the general Q&A agent."""
        self.name = "General Q&A"

    def answer(self, user_question: str, context: str = None) -> Dict[str, Any]:
        """
        Generate a bilingual answer to a general question with conversation context.

        Args:
            user_question: The question to answer
            context: Recent conversation context (optional)

        Returns:
            Dictionary containing:
                - english_answer: Answer in English
                - arabic_answer: Answer in Arabic
                - category: Type of question (e.g., "advice", "how-to", "factual")
                - confidence: Confidence level in the answer
                - follow_up_suggestions: List of related questions (optional)

        Raises:
            Exception: If answer generation fails
        """
        try:
            # Format the user prompt with context
            if context and context.strip():
                user_prompt = GENERAL_QA_USER_PROMPT_TEMPLATE.format(
                    context=context,
                    user_question=user_question
                )
            else:
                # No context available - use basic template
                from prompts.general_qa_prompts import GENERAL_QA_USER_PROMPT_NO_CONTEXT
                user_prompt = GENERAL_QA_USER_PROMPT_NO_CONTEXT.format(
                    user_question=user_question
                )

            # Call LLM for answer generation
            result = llm_client.generate_json_completion(
                system_prompt=GENERAL_QA_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                temperature=0.7,
                max_tokens=1500
            )

            # Validate the result
            is_valid, error_msg = validators.validate_general_qa_result(result)
            if not is_valid:
                raise ValueError(f"Invalid Q&A result: {error_msg}")

            # Ensure all expected fields exist with defaults
            result.setdefault("category", "general")
            result.setdefault("confidence", 0.8)
            result.setdefault("follow_up_suggestions", [])

            return result

        except Exception as e:
            raise Exception(f"General Q&A agent failed: {str(e)}")


# Global instance
general_qa_agent = GeneralQAAgent()
