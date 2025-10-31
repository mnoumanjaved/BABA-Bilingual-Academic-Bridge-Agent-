"""
LLM Client Wrapper for OpenAI API.

Provides a unified interface for interacting with OpenAI's API,
including error handling, retries, and response parsing.
"""

import json
import time
from typing import Dict, Any, Optional, List
from openai import OpenAI
from config import config


class LLMClient:
    """Wrapper class for OpenAI API interactions."""

    def __init__(self):
        """Initialize the OpenAI client."""
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)
        self.model = config.OPENAI_MODEL
        self.max_retries = 3
        self.retry_delay = 2  # seconds

    def generate_completion(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = None,
        max_tokens: int = None,
        response_format: Optional[str] = None
    ) -> str:
        """
        Generate a completion from OpenAI API.

        Args:
            system_prompt: System message defining agent behavior
            user_prompt: User message with the actual request
            temperature: Sampling temperature (0-2)
            max_tokens: Maximum tokens in response
            response_format: Optional format specification ("json_object" for JSON)

        Returns:
            Generated text response

        Raises:
            Exception: If API call fails after retries
        """
        temperature = temperature if temperature is not None else config.TEMPERATURE
        max_tokens = max_tokens if max_tokens is not None else config.MAX_TOKENS

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        for attempt in range(self.max_retries):
            try:
                kwargs = {
                    "model": self.model,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens
                }

                if response_format == "json_object":
                    kwargs["response_format"] = {"type": "json_object"}

                response = self.client.chat.completions.create(**kwargs)

                return response.choices[0].message.content.strip()

            except Exception as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                    continue
                else:
                    raise Exception(f"API call failed after {self.max_retries} attempts: {str(e)}")

    def generate_json_completion(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = None,
        max_tokens: int = None
    ) -> Dict[str, Any]:
        """
        Generate a JSON-formatted completion from OpenAI API.

        Args:
            system_prompt: System message defining agent behavior
            user_prompt: User message with the actual request
            temperature: Sampling temperature (0-2)
            max_tokens: Maximum tokens in response

        Returns:
            Parsed JSON response as dictionary

        Raises:
            Exception: If API call fails or JSON parsing fails
        """
        response_text = self.generate_completion(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format="json_object"
        )

        try:
            return json.loads(response_text)
        except json.JSONDecodeError as e:
            # Fallback: try to extract JSON from response
            try:
                # Sometimes the model returns JSON wrapped in markdown code blocks
                if "```json" in response_text:
                    json_str = response_text.split("```json")[1].split("```")[0].strip()
                    return json.loads(json_str)
                elif "```" in response_text:
                    json_str = response_text.split("```")[1].split("```")[0].strip()
                    return json.loads(json_str)
                else:
                    raise e
            except Exception:
                raise Exception(f"Failed to parse JSON response: {response_text[:200]}...")

    def generate_with_history(
        self,
        messages: List[Dict[str, str]],
        temperature: float = None,
        max_tokens: int = None
    ) -> str:
        """
        Generate a completion with conversation history.

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            temperature: Sampling temperature (0-2)
            max_tokens: Maximum tokens in response

        Returns:
            Generated text response
        """
        temperature = temperature if temperature is not None else config.TEMPERATURE
        max_tokens = max_tokens if max_tokens is not None else config.MAX_TOKENS

        for attempt in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens
                )

                return response.choices[0].message.content.strip()

            except Exception as e:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                    continue
                else:
                    raise Exception(f"API call failed after {self.max_retries} attempts: {str(e)}")


# Global LLM client instance
llm_client = LLMClient()
