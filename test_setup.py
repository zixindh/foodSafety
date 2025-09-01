#!/usr/bin/env python3
"""
Food Safety Analyzer - Setup Test Script
Tests the configuration and API connectivity
"""

import os
import sys
from dotenv import load_dotenv
import requests
from PIL import Image
import io

def test_env_file():
    """Test if .env file exists and contains required variables."""
    print("🔍 Testing environment configuration...")

    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        return False

    load_dotenv()

    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ OPENROUTER_API_KEY not found in .env file!")
        return False

    if not api_key.startswith('sk-or-v1-'):
        print("⚠️  Warning: API key doesn't start with 'sk-or-v1-'. Please verify it's correct.")

    print("✅ Environment configuration looks good!")
    return True

def test_dependencies():
    """Test if all required dependencies are installed."""
    print("\n🔍 Testing dependencies...")

    required_packages = ['streamlit', 'pillow', 'python-dotenv', 'requests']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} - MISSING")

    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Please run: pip install -r requirements.txt")
        return False

    print("✅ All dependencies are installed!")
    return True

def test_api_connectivity():
    """Test OpenRouter API connectivity."""
    print("\n🔍 Testing API connectivity...")

    load_dotenv()
    api_key = os.getenv('OPENROUTER_API_KEY')

    if not api_key:
        print("❌ No API key found!")
        return False

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # Simple test request
        payload = {
            "model": "google/gemini-2.0-flash-001",
            "messages": [
                {
                    "role": "user",
                    "content": "Hello, this is a test message."
                }
            ],
            "max_tokens": 10
        }

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=10
        )

        if response.status_code == 200:
            print("✅ API connection successful!")
            return True
        else:
            print(f"❌ API connection failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        return False

def test_image_processing():
    """Test image processing capabilities."""
    print("\n🔍 Testing image processing...")

    try:
        # Create a simple test image
        img = Image.new('RGB', (100, 100), color='red')
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)

        # Test resizing
        resized_img = img.resize((50, 50), Image.Resampling.LANCZOS)
        print("✅ Image processing works!")

        return True
    except Exception as e:
        print(f"❌ Image processing test failed: {str(e)}")
        return False

def main():
    """Run all tests."""
    print("🍎 Food Safety Analyzer - Setup Test")
    print("=" * 40)

    tests = [
        test_env_file,
        test_dependencies,
        test_api_connectivity,
        test_image_processing
    ]

    results = []
    for test in tests:
        results.append(test())

    print("\n" + "=" * 40)
    print("📊 Test Results:")

    passed = sum(results)
    total = len(results)

    if passed == total:
        print(f"✅ All tests passed! ({passed}/{total})")
        print("\n🚀 You're ready to run the app!")
        print("Execute: streamlit run app.py")
    else:
        print(f"❌ Some tests failed: {passed}/{total} passed")
        print("\n🔧 Please fix the issues above before running the app.")

    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
