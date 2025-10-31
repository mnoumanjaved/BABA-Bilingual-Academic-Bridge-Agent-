"""
BABA Agent Testing Script

Run this script to test individual agents with sample inputs.
This helps verify that each agent is working correctly.
"""

import sys
from config import config

def test_task_classifier():
    """Test the task classifier agent."""
    print("\n" + "="*60)
    print("Testing Task Classifier Agent")
    print("="*60)

    try:
        from agents.task_classifier import task_classifier

        test_cases = [
            "What is critical thinking?",
            "The research is show that climate change effect economy.",
            "Explain the concept of sustainability"
        ]

        for i, test_input in enumerate(test_cases, 1):
            print(f"\nTest {i}: {test_input}")
            result = task_classifier.classify(test_input)
            print(f"  Task Type: {result['task_type']}")
            print(f"  Confidence: {result['confidence']:.2%}")
            print(f"  Language: {result.get('detected_language', 'unknown')}")

        print("\n✓ Task Classifier: PASSED")
        return True

    except Exception as e:
        print(f"\n✗ Task Classifier: FAILED - {str(e)}")
        return False

def test_explainer_agent():
    """Test the explainer agent."""
    print("\n" + "="*60)
    print("Testing Explainer Agent")
    print("="*60)

    try:
        from agents.explainer_agent import explainer_agent

        test_input = "What is critical thinking?"
        print(f"\nTest Input: {test_input}")
        print("Generating explanation... (this may take 5-10 seconds)")

        result = explainer_agent.explain(test_input)

        print("\nResult:")
        print(f"  English Explanation: {result['english_explanation'][:100]}...")
        print(f"  Arabic Explanation: {result['arabic_explanation'][:100]}...")
        print(f"  Gulf Example: {result.get('gulf_example', 'N/A')[:100]}...")

        print("\n✓ Explainer Agent: PASSED")
        return True

    except Exception as e:
        print(f"\n✗ Explainer Agent: FAILED - {str(e)}")
        return False

def test_writer_agent():
    """Test the writer agent."""
    print("\n" + "="*60)
    print("Testing Writer Agent")
    print("="*60)

    try:
        from agents.writer_agent import writer_agent

        test_input = "The research is show that climate change effect economy."
        print(f"\nTest Input: {test_input}")
        print("Improving writing... (this may take 5-10 seconds)")

        result = writer_agent.improve(test_input)

        print("\nResult:")
        print(f"  Improved Text: {result['improved_text']}")
        print(f"  Changes (Arabic): {result['changes_explanation_ar'][:100]}...")

        print("\n✓ Writer Agent: PASSED")
        return True

    except Exception as e:
        print(f"\n✗ Writer Agent: FAILED - {str(e)}")
        return False

def test_quiz_agent():
    """Test the quiz agent."""
    print("\n" + "="*60)
    print("Testing Quiz Agent")
    print("="*60)

    try:
        from agents.quiz_agent import quiz_agent

        test_content = """
        Critical thinking is the ability to analyze information objectively
        and make reasoned judgments. It involves evaluating sources,
        identifying biases, and considering multiple perspectives.
        """

        print("\nGenerating quiz... (this may take 5-10 seconds)")
        result = quiz_agent.generate(test_content)

        print(f"\nResult: Generated {len(result['questions'])} questions")
        for i, q in enumerate(result['questions'], 1):
            print(f"\nQuestion {i}:")
            print(f"  EN: {q['question_en']}")
            print(f"  AR: {q['question_ar']}")
            print(f"  Options: {len(q['options'])}")

        print("\n✓ Quiz Agent: PASSED")
        return True

    except Exception as e:
        print(f"\n✗ Quiz Agent: FAILED - {str(e)}")
        return False

def test_orchestrator():
    """Test the orchestrator with full workflow."""
    print("\n" + "="*60)
    print("Testing Orchestrator (Full Workflow)")
    print("="*60)

    try:
        from agents.orchestrator import orchestrator

        test_input = "What is critical thinking?"
        print(f"\nTest Input: {test_input}")
        print("Processing through orchestrator... (this may take 10-15 seconds)")

        result = orchestrator.process_user_input(test_input)

        if result.get('error'):
            print(f"\n✗ Orchestrator: FAILED - {result['error']}")
            return False

        print("\nResult:")
        print(f"  Classification: {result['classification']['task_type']}")
        print(f"  Autonomous Actions: {len(result['autonomous_actions'])}")
        print(f"  Main Result Type: {result['main_result']['type']}")

        # List autonomous actions
        print("\n  Autonomous Actions Taken:")
        for action in result['autonomous_actions']:
            print(f"    - {action['agent']}: {action['action']}")

        print("\n✓ Orchestrator: PASSED")
        return True

    except Exception as e:
        print(f"\n✗ Orchestrator: FAILED - {str(e)}")
        return False

def main():
    """Run all agent tests."""
    print("="*60)
    print("BABA Agent Testing Suite")
    print("="*60)

    # Validate configuration
    try:
        config.validate()
        print("\n✓ Configuration validated")
    except Exception as e:
        print(f"\n✗ Configuration error: {str(e)}")
        print("\nPlease fix the configuration before testing agents.")
        print("See QUICKSTART.md for setup instructions.")
        return 1

    print("\nThis will test all agents with sample inputs.")
    print("Each test may take 5-15 seconds due to API calls.")
    print("\nNote: These tests will use your OpenAI API credits.")

    response = input("\nProceed with testing? (y/n): ")
    if response.lower() != 'y':
        print("Testing cancelled.")
        return 0

    # Run all tests
    results = {
        "Task Classifier": test_task_classifier(),
        "Explainer Agent": test_explainer_agent(),
        "Writer Agent": test_writer_agent(),
        "Quiz Agent": test_quiz_agent(),
        "Orchestrator": test_orchestrator()
    }

    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)

    for test_name, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{test_name:.<40} {status}")

    print("="*60)

    if all(results.values()):
        print("\n🎉 ALL TESTS PASSED!")
        print("BABA is fully functional and ready to use.")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED")
        print("Please check the errors above and fix any issues.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
