"""
Message History Utility.

Manages persistent storage of recent user messages using browser localStorage.
Maintains the last 5 user messages across sessions.
"""

import json
from typing import List
import streamlit as st
import streamlit.components.v1 as components


class MessageHistory:
    """Manages persistent message history using browser localStorage via JavaScript."""

    def __init__(self, max_messages: int = 5):
        """
        Initialize message history manager.

        Args:
            max_messages: Maximum number of recent messages to store (default: 5)
        """
        self.max_messages = max_messages
        self.storage_key = "baba_recent_messages"

    def _get_localStorage_component(self, mode: str, value: str = None) -> str:
        """
        Generate JavaScript code for localStorage operations.

        Args:
            mode: 'get', 'set', or 'clear'
            value: Value to set (for 'set' mode)

        Returns:
            JavaScript code as string
        """
        if mode == "get":
            return f"""
            <script>
                var messages = localStorage.getItem('{self.storage_key}');
                var streamlit = window.parent.document.querySelector('iframe').contentWindow;
                streamlit.postMessage({{
                    type: 'streamlit:setComponentValue',
                    value: messages
                }}, '*');
            </script>
            """
        elif mode == "set":
            value_json = json.dumps(value)
            return f"""
            <script>
                localStorage.setItem('{self.storage_key}', '{value_json}');
            </script>
            """
        elif mode == "clear":
            return f"""
            <script>
                localStorage.removeItem('{self.storage_key}');
            </script>
            """

    def get_recent_messages(self) -> List[str]:
        """
        Retrieve recent user messages from localStorage.

        Returns:
            List of recent user message strings (up to max_messages)
        """
        try:
            # Use session state as cache
            if 'message_history_cache' not in st.session_state:
                st.session_state.message_history_cache = []

            return st.session_state.message_history_cache[-self.max_messages:]

        except Exception as e:
            # If there's any error, return empty list
            return []

    def add_message(self, message: str) -> None:
        """
        Add a new user message to history.

        Args:
            message: The user message to add
        """
        try:
            # Get existing messages from session state cache
            if 'message_history_cache' not in st.session_state:
                st.session_state.message_history_cache = []

            messages = st.session_state.message_history_cache

            # Add new message
            messages.append(message)

            # Keep only the last N messages
            messages = messages[-self.max_messages:]

            # Update session state
            st.session_state.message_history_cache = messages

            # Save to localStorage (non-blocking)
            messages_json = json.dumps(messages)
            self._save_to_localStorage(messages_json)

        except Exception as e:
            # Fail silently - message history is not critical
            pass

    def _save_to_localStorage(self, value: str) -> None:
        """
        Save data to browser localStorage (non-blocking).

        Args:
            value: JSON string to save
        """
        try:
            html_code = f"""
            <script>
                localStorage.setItem('{self.storage_key}', '{value}');
            </script>
            """
            components.html(html_code, height=0, width=0)
        except Exception:
            pass

    def clear_history(self) -> None:
        """Clear all message history."""
        try:
            # Clear session state
            if 'message_history_cache' in st.session_state:
                st.session_state.message_history_cache = []

            # Clear localStorage
            html_code = f"""
            <script>
                localStorage.removeItem('{self.storage_key}');
            </script>
            """
            components.html(html_code, height=0, width=0)

        except Exception:
            pass

    def get_context_summary(self) -> str:
        """
        Get a formatted summary of recent messages for context.

        Returns:
            Formatted string with recent messages
        """
        messages = self.get_recent_messages()

        if not messages:
            return "No recent message history."

        summary = "Recent conversation context:\n"
        for i, msg in enumerate(messages, 1):
            # Truncate long messages
            truncated = msg[:100] + "..." if len(msg) > 100 else msg
            summary += f"{i}. {truncated}\n"

        return summary


# Global instance
message_history = MessageHistory(max_messages=5)
