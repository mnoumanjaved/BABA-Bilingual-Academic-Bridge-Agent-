"""
Arabic Text Processing Utilities.

Provides functions for detecting, validating, and processing Arabic text.
"""

import re
from langdetect import detect, LangDetectException
from typing import Tuple


class ArabicUtils:
    """Utility class for Arabic text processing."""

    # Arabic Unicode ranges
    ARABIC_RANGE = r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]'

    @staticmethod
    def contains_arabic(text: str) -> bool:
        """
        Check if text contains Arabic characters.

        Args:
            text: Input text to check

        Returns:
            True if text contains Arabic characters, False otherwise
        """
        if not text:
            return False
        return bool(re.search(ArabicUtils.ARABIC_RANGE, text))

    @staticmethod
    def contains_english(text: str) -> bool:
        """
        Check if text contains English characters.

        Args:
            text: Input text to check

        Returns:
            True if text contains English characters, False otherwise
        """
        if not text:
            return False
        return bool(re.search(r'[a-zA-Z]', text))

    @staticmethod
    def detect_language(text: str) -> str:
        """
        Detect the primary language of the text.

        Args:
            text: Input text to analyze

        Returns:
            Language code ('ar' for Arabic, 'en' for English, 'mixed' for both, 'unknown' if unclear)
        """
        if not text or len(text.strip()) < 3:
            return "unknown"

        has_arabic = ArabicUtils.contains_arabic(text)
        has_english = ArabicUtils.contains_english(text)

        if has_arabic and has_english:
            return "mixed"
        elif has_arabic:
            return "ar"
        elif has_english:
            return "en"

        # Fallback to langdetect
        try:
            detected = detect(text)
            return detected if detected in ['ar', 'en'] else "unknown"
        except LangDetectException:
            return "unknown"

    @staticmethod
    def get_text_direction(text: str) -> str:
        """
        Determine text direction (RTL for Arabic, LTR for English).

        Args:
            text: Input text

        Returns:
            'rtl' for right-to-left, 'ltr' for left-to-right
        """
        lang = ArabicUtils.detect_language(text)
        return "rtl" if lang in ['ar', 'mixed'] else "ltr"

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean and normalize text.

        Args:
            text: Input text

        Returns:
            Cleaned text
        """
        if not text:
            return ""

        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)

        # Strip leading/trailing whitespace
        text = text.strip()

        return text

    @staticmethod
    def extract_arabic_percentage(text: str) -> float:
        """
        Calculate the percentage of Arabic characters in the text.

        Args:
            text: Input text

        Returns:
            Percentage of Arabic characters (0.0 to 100.0)
        """
        if not text:
            return 0.0

        arabic_chars = len(re.findall(ArabicUtils.ARABIC_RANGE, text))
        total_chars = len(re.findall(r'\S', text))  # Non-whitespace characters

        if total_chars == 0:
            return 0.0

        return (arabic_chars / total_chars) * 100

    @staticmethod
    def is_primarily_arabic(text: str, threshold: float = 50.0) -> bool:
        """
        Check if text is primarily in Arabic.

        Args:
            text: Input text
            threshold: Percentage threshold for considering text as primarily Arabic

        Returns:
            True if Arabic percentage exceeds threshold
        """
        return ArabicUtils.extract_arabic_percentage(text) >= threshold

    @staticmethod
    def split_bilingual_text(text: str) -> Tuple[str, str]:
        """
        Attempt to split mixed Arabic-English text.

        Args:
            text: Mixed language text

        Returns:
            Tuple of (english_part, arabic_part)
        """
        lines = text.split('\n')
        english_parts = []
        arabic_parts = []

        for line in lines:
            if ArabicUtils.is_primarily_arabic(line):
                arabic_parts.append(line)
            else:
                english_parts.append(line)

        return '\n'.join(english_parts).strip(), '\n'.join(arabic_parts).strip()


# Global instance
arabic_utils = ArabicUtils()
