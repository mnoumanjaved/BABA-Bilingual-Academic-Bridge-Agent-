"""
BABA Setup Verification Script

Run this script to verify that your BABA installation is correctly configured.
"""

import sys
import os
from pathlib import Path

def print_status(message, status):
    """Print colored status message."""
    if status == "OK":
        print(f"✓ {message}")
    elif status == "WARNING":
        print(f"⚠ {message}")
    elif status == "ERROR":
        print(f"✗ {message}")
    else:
        print(f"  {message}")

def check_python_version():
    """Check if Python version is compatible."""
    print("\n=== Checking Python Version ===")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print_status(f"Python {version.major}.{version.minor}.{version.micro} detected", "OK")
        return True
    else:
        print_status(f"Python {version.major}.{version.minor} - Need Python 3.8+", "ERROR")
        return False

def check_dependencies():
    """Check if required packages are installed."""
    print("\n=== Checking Dependencies ===")
    required_packages = [
        "streamlit",
        "openai",
        "dotenv",
        "langdetect",
        "pydantic"
    ]

    all_installed = True
    for package in required_packages:
        try:
            if package == "dotenv":
                __import__("dotenv")
            else:
                __import__(package)
            print_status(f"{package} installed", "OK")
        except ImportError:
            print_status(f"{package} NOT installed", "ERROR")
            all_installed = False

    if not all_installed:
        print("\n💡 Install missing packages with: pip install -r requirements.txt")

    return all_installed

def check_project_structure():
    """Check if all required files and directories exist."""
    print("\n=== Checking Project Structure ===")

    required_items = {
        "files": [
            "app.py",
            "config.py",
            "requirements.txt",
            ".env",
            "README.md"
        ],
        "directories": [
            "agents",
            "prompts",
            "utils"
        ]
    }

    all_present = True

    # Check files
    for file in required_items["files"]:
        if Path(file).exists():
            print_status(f"{file} found", "OK")
        else:
            print_status(f"{file} NOT found", "ERROR")
            all_present = False

    # Check directories
    for directory in required_items["directories"]:
        if Path(directory).is_dir():
            print_status(f"{directory}/ directory found", "OK")
        else:
            print_status(f"{directory}/ directory NOT found", "ERROR")
            all_present = False

    return all_present

def check_env_configuration():
    """Check if .env file is properly configured."""
    print("\n=== Checking Environment Configuration ===")

    try:
        from dotenv import load_dotenv
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")
        model = os.getenv("OPENAI_MODEL")

        if not api_key:
            print_status("OPENAI_API_KEY not set in .env", "ERROR")
            print("  💡 Edit .env file and add your OpenAI API key")
            return False

        if api_key == "your_openai_api_key_here":
            print_status("OPENAI_API_KEY still has placeholder value", "ERROR")
            print("  💡 Replace placeholder with your actual API key")
            return False

        if not api_key.startswith("sk-"):
            print_status("OPENAI_API_KEY format looks incorrect", "WARNING")
            print("  💡 OpenAI keys typically start with 'sk-'")
            return False

        print_status("OPENAI_API_KEY is set", "OK")

        if model:
            print_status(f"Model configured: {model}", "OK")
        else:
            print_status("OPENAI_MODEL not set (will use default)", "WARNING")

        return True

    except Exception as e:
        print_status(f"Error checking .env: {str(e)}", "ERROR")
        return False

def check_agent_modules():
    """Check if agent modules can be imported."""
    print("\n=== Checking Agent Modules ===")

    modules = [
        "agents.orchestrator",
        "agents.task_classifier",
        "agents.explainer_agent",
        "agents.writer_agent",
        "agents.quiz_agent",
        "agents.feedback_agent"
    ]

    all_importable = True
    for module in modules:
        try:
            __import__(module)
            print_status(f"{module} can be imported", "OK")
        except Exception as e:
            print_status(f"{module} import failed: {str(e)}", "ERROR")
            all_importable = False

    return all_importable

def test_api_connection():
    """Test if OpenAI API connection works."""
    print("\n=== Testing API Connection ===")

    try:
        from config import config
        config.validate()

        from utils.llm_client import llm_client

        print("  Attempting test API call...")
        response = llm_client.generate_completion(
            system_prompt="You are a helpful assistant.",
            user_prompt="Say 'Hello' in one word.",
            max_tokens=10
        )

        if response:
            print_status("API connection successful", "OK")
            print(f"  Response: {response}")
            return True
        else:
            print_status("API returned empty response", "WARNING")
            return False

    except Exception as e:
        print_status(f"API connection failed: {str(e)}", "ERROR")
        print("  💡 Check your API key and internet connection")
        return False

def main():
    """Run all verification checks."""
    print("=" * 60)
    print("BABA Setup Verification")
    print("=" * 60)

    results = {
        "Python Version": check_python_version(),
        "Dependencies": check_dependencies(),
        "Project Structure": check_project_structure(),
        "Environment Config": check_env_configuration(),
        "Agent Modules": check_agent_modules()
    }

    # Only test API if other checks pass
    if all(results.values()):
        results["API Connection"] = test_api_connection()
    else:
        print("\n=== Skipping API Test ===")
        print("  Fix the errors above before testing API connection")
        results["API Connection"] = False

    # Summary
    print("\n" + "=" * 60)
    print("VERIFICATION SUMMARY")
    print("=" * 60)

    for check, status in results.items():
        status_str = "✓ PASS" if status else "✗ FAIL"
        print(f"{check:.<40} {status_str}")

    print("=" * 60)

    if all(results.values()):
        print("\n🎉 SUCCESS! BABA is properly configured and ready to use!")
        print("\nNext steps:")
        print("  1. Run: streamlit run app.py")
        print("  2. Open browser to http://localhost:8501")
        print("  3. Try asking BABA a question!")
        return 0
    else:
        print("\n❌ SETUP INCOMPLETE - Please fix the errors above")
        print("\nCommon fixes:")
        print("  • Install dependencies: pip install -r requirements.txt")
        print("  • Add API key to .env file")
        print("  • Check QUICKSTART.md for detailed instructions")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
