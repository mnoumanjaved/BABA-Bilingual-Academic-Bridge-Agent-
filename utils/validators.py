"""
Input Validation Utilities.

Provides validation functions for user inputs and agent responses.
"""

from typing import Optional, Dict, Any


class Validators:
    """Validation utility class."""

    @staticmethod
    def validate_user_input(text: str) -> tuple[bool, Optional[str]]:
        """
        Validate user input text.

        Args:
            text: User input to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not text:
            return False, "Input cannot be empty."

        if len(text.strip()) < 3:
            return False, "Input is too short. Please provide at least 3 characters."

        if len(text) > 5000:
            return False, "Input is too long. Please limit to 5000 characters."

        return True, None

    @staticmethod
    def validate_task_classification(result: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        Validate task classification result.

        Args:
            result: Classification result dictionary

        Returns:
            Tuple of (is_valid, error_message)
        """
        required_fields = ["task_type", "confidence"]

        for field in required_fields:
            if field not in result:
                return False, f"Missing required field: {field}"

        valid_task_types = ["explanation", "writing_improvement"]
        if result["task_type"] not in valid_task_types:
            return False, f"Invalid task type: {result['task_type']}"

        if not isinstance(result["confidence"], (int, float)):
            return False, "Confidence must be a number"

        if not 0 <= result["confidence"] <= 1:
            return False, "Confidence must be between 0 and 1"

        return True, None

    @staticmethod
    def validate_explanation_result(result: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        Validate explanation agent result.

        Args:
            result: Explanation result dictionary

        Returns:
            Tuple of (is_valid, error_message)
        """
        required_fields = ["english_explanation", "arabic_explanation"]

        for field in required_fields:
            if field not in result:
                return False, f"Missing required field: {field}"

            if not isinstance(result[field], str):
                return False, f"Field {field} must be a string"

            if len(result[field].strip()) < 10:
                return False, f"Field {field} is too short"

        return True, None

    @staticmethod
    def validate_writing_result(result: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        Validate writing improvement result.

        Args:
            result: Writing improvement result dictionary

        Returns:
            Tuple of (is_valid, error_message)
        """
        required_fields = ["improved_text", "changes_explanation_ar"]

        for field in required_fields:
            if field not in result:
                return False, f"Missing required field: {field}"

            if not isinstance(result[field], str):
                return False, f"Field {field} must be a string"

            if len(result[field].strip()) < 5:
                return False, f"Field {field} is too short"

        return True, None

    @staticmethod
    def validate_quiz_result(result: Dict[str, Any]) -> tuple[bool, Optional[str]]:
        """
        Validate quiz generation result.

        Args:
            result: Quiz result dictionary

        Returns:
            Tuple of (is_valid, error_message)
        """
        if "questions" not in result:
            return False, "Missing questions field"

        if not isinstance(result["questions"], list):
            return False, "Questions must be a list"

        if len(result["questions"]) == 0:
            return False, "Questions list cannot be empty"

        for i, question in enumerate(result["questions"]):
            required_fields = ["question_en", "question_ar", "options", "correct_answer"]

            for field in required_fields:
                if field not in question:
                    return False, f"Question {i+1} missing field: {field}"

            if not isinstance(question["options"], list):
                return False, f"Question {i+1}: options must be a list"

            if len(question["options"]) < 2:
                return False, f"Question {i+1}: must have at least 2 options"

            if not isinstance(question["correct_answer"], int):
                return False, f"Question {i+1}: correct_answer must be an integer"

            if question["correct_answer"] < 0 or question["correct_answer"] >= len(question["options"]):
                return False, f"Question {i+1}: correct_answer index out of range"

        return True, None


# Global instance
validators = Validators()
