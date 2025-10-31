"""
Explainer Agent.

Provides bilingual academic explanations of concepts and terms.
"""

from typing import Dict, Any
from utils.llm_client import llm_client
from utils.validators import validators
from prompts.explainer_prompts import (
    EXPLAINER_SYSTEM_PROMPT,
    EXPLAINER_USER_PROMPT_TEMPLATE
)


class ExplainerAgent:
    """Agent responsible for explaining academic concepts bilingually."""

    def __init__(self):
        """Initialize the explainer agent."""
        self.name = "Explainer"

    def explain(self, user_input: str) -> Dict[str, Any]:
        """
        Generate a bilingual explanation of a concept.

        Args:
            user_input: The concept or term to explain

        Returns:
            Dictionary containing:
                - english_explanation: Explanation in English
                - arabic_explanation: Explanation in Arabic
                - gulf_example: Example relevant to Gulf region
                - key_terms: List of important terms
                - suggested_next_step: Recommendation for further learning

        Raises:
            Exception: If explanation generation fails
        """
        try:
            # Format the user prompt
            user_prompt = EXPLAINER_USER_PROMPT_TEMPLATE.format(
                user_input=user_input
            )

            # Call LLM for explanation
            result = llm_client.generate_json_completion(
                system_prompt=EXPLAINER_SYSTEM_PROMPT,
                user_prompt=user_prompt,
                temperature=0.7,
                max_tokens=2000
            )

            # Validate the result
            is_valid, error_msg = validators.validate_explanation_result(result)
            if not is_valid:
                raise ValueError(f"Invalid explanation result: {error_msg}")

            # Ensure all expected fields exist with defaults if needed
            result.setdefault("gulf_example", "No specific example provided.")
            result.setdefault("key_terms", [])
            result.setdefault("suggested_next_step", "Practice using this concept in your own writing.")

            return result

        except Exception as e:
            raise Exception(f"Explainer agent failed: {str(e)}")


# Global instance
explainer_agent = ExplainerAgent()
