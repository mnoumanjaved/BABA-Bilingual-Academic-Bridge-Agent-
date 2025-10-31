"""
Writer Agent.

Improves academic writing and provides feedback in Arabic.
"""

from typing import Dict, Any
from utils.llm_client import llm_client
from utils.validators import validators
from prompts.writer_prompts import (
    WRITER_SYSTEM_PROMPT,
    WRITER_USER_PROMPT_TEMPLATE
)


class WriterAgent:
    """Agent responsible for improving academic writing."""

    def __init__(self):
        """Initialize the writer agent."""
        self.name = "Writer"

    def improve(self, user_input: str) -> Dict[str, Any]:
        """
        Improve academic writing and explain changes.

        Args:
            user_input: The text to improve

        Returns:
            Dictionary containing:
                - improved_text: Rewritten text in formal academic English
                - changes_explanation_ar: Explanation of changes in Arabic
                - grammar_points: List of grammar improvements made
                - tone_improvements: List of tone/style improvements
                - suggested_next_step: Recommendation for further improvement

        Raises:
            Exception: If writing improvement fails
        """
        try:
            # Format the user prompt
            user_prompt = WRITER_USER_PROMPT_TEMPLATE.format(
                user_input=user_input
            )

            # Call LLM for writing improvement
            result = llm_client.generate_json_completion(
                system_prompt=WRITER_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                temperature=0.5,  # Moderate temperature for balanced creativity and consistency
                max_tokens=2000
            )

            # Validate the result
            is_valid, error_msg = validators.validate_writing_result(result)
            if not is_valid:
                raise ValueError(f"Invalid writing result: {error_msg}")

            # Ensure all expected fields exist with defaults if needed
            result.setdefault("grammar_points", [])
            result.setdefault("tone_improvements", [])
            result.setdefault("suggested_next_step", "Continue practicing formal academic writing.")

            return result

        except Exception as e:
            raise Exception(f"Writer agent failed: {str(e)}")


# Global instance
writer_agent = WriterAgent()
