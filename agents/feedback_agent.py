"""
Feedback Agent.

Analyzes student progress and provides learning path suggestions.
"""

from typing import Dict, Any, List


class FeedbackAgent:
    """Agent responsible for providing feedback and learning suggestions."""

    def __init__(self):
        """Initialize the feedback agent."""
        self.name = "Feedback"

    def analyze_quiz_performance(
        self,
        total_questions: int,
        correct_answers: int
    ) -> Dict[str, Any]:
        """
        Analyze quiz performance and provide feedback.

        Args:
            total_questions: Total number of questions
            correct_answers: Number of correct answers

        Returns:
            Dictionary with:
                - score_percentage: Score as percentage
                - performance_level: "excellent", "good", "needs_improvement"
                - feedback: Personalized feedback message
                - suggestion: What to do next
        """
        if total_questions == 0:
            return {
                "score_percentage": 0,
                "performance_level": "unknown",
                "feedback": "No quiz attempted yet.",
                "suggestion": "Try taking a quiz to test your understanding."
            }

        score_percentage = (correct_answers / total_questions) * 100

        if score_percentage >= 80:
            performance_level = "excellent"
            feedback = "Excellent work! You have a strong understanding of the concept."
            feedback_ar = "عمل ممتاز! لديك فهم قوي للمفهوم."
            suggestion = "Move on to more advanced topics or practice applying this concept."
        elif score_percentage >= 60:
            performance_level = "good"
            feedback = "Good job! You understand the basics, but there's room for improvement."
            feedback_ar = "عمل جيد! تفهم الأساسيات، ولكن هناك مجال للتحسين."
            suggestion = "Review the areas you struggled with and try another quiz."
        else:
            performance_level = "needs_improvement"
            feedback = "You need more practice with this concept."
            feedback_ar = "تحتاج إلى مزيد من الممارسة مع هذا المفهوم."
            suggestion = "Review the explanation carefully and ask for clarification on confusing points."

        return {
            "score_percentage": score_percentage,
            "performance_level": performance_level,
            "feedback": feedback,
            "feedback_ar": feedback_ar,
            "suggestion": suggestion
        }

    def suggest_learning_path(
        self,
        task_type: str,
        interaction_history: List[str] = None
    ) -> Dict[str, Any]:
        """
        Suggest next steps in the learning journey.

        Args:
            task_type: Type of task completed
            interaction_history: List of previous interactions

        Returns:
            Dictionary with learning path suggestions
        """
        suggestions = {
            "explanation": {
                "next_steps": [
                    "Take a quiz to test your understanding",
                    "Practice using this concept in a sentence",
                    "Find real-world examples of this concept"
                ],
                "next_steps_ar": [
                    "خذ اختبارًا لاختبار فهمك",
                    "تدرب على استخدام هذا المفهوم في جملة",
                    "ابحث عن أمثلة واقعية لهذا المفهوم"
                ]
            },
            "writing_improvement": {
                "next_steps": [
                    "Practice the grammar points highlighted",
                    "Rewrite another paragraph using formal academic tone",
                    "Read academic papers in your field to learn the style"
                ],
                "next_steps_ar": [
                    "تدرب على نقاط القواعد المذكورة",
                    "أعد كتابة فقرة أخرى باستخدام أسلوب أكاديمي رسمي",
                    "اقرأ الأوراق الأكاديمية في مجالك لتعلم الأسلوب"
                ]
            }
        }

        return suggestions.get(task_type, suggestions["explanation"])

    def generate_encouragement(self, performance_level: str) -> str:
        """
        Generate encouraging message based on performance.

        Args:
            performance_level: "excellent", "good", or "needs_improvement"

        Returns:
            Encouraging message
        """
        messages = {
            "excellent": "Keep up the excellent work! You're making great progress.",
            "good": "You're doing well! Keep practicing and you'll improve even more.",
            "needs_improvement": "Don't give up! Learning takes time and practice. You can do this!"
        }

        return messages.get(performance_level, "Keep learning and practicing!")


# Global instance
feedback_agent = FeedbackAgent()
