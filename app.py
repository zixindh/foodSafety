import streamlit as st
import os
from PIL import Image
import io
import base64
import requests
from dotenv import load_dotenv
import json
from typing import Optional, Tuple

# Load environment variables
load_dotenv()

# Constants
MAX_IMAGE_SIZE = 20 * 1024 * 1024  # 20MB
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
SUPPORTED_FORMATS = ['png', 'jpg', 'jpeg', 'webp', 'gif']

# Page configuration
st.set_page_config(
    page_title="Food Safety Analyzer",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Compact CSS
st.markdown("""
<style>
    .main {padding: 1rem; max-width: 1000px; margin: 0 auto;}
    .upload-section {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border: 2px dashed #dee2e6;
    }
    .result-section {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #2196f3;
    }
    .stButton>button {
        background: #2196f3;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 6px;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

def get_api_key() -> str:
    """Get OpenRouter API key from environment variables."""
    api_key = os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        st.error("❌ OpenRouter API key not found. Please set OPENROUTER_API_KEY in your .env file.")
        st.stop()
    return api_key

def resize_and_compress_image(image: Image.Image, max_size_mb: int = 20) -> bytes:
    """Resize and compress image to under specified MB limit."""
    # Convert to RGB if necessary
    if image.mode in ("RGBA", "LA", "P"):
        image = image.convert("RGB")

    # Simple approach: resize to reasonable dimensions first
    max_width, max_height = 1024, 1024
    if image.width > max_width or image.height > max_height:
        ratio = min(max_width / image.width, max_height / image.height)
        new_size = (int(image.width * ratio), int(image.height * ratio))
        image = image.resize(new_size, Image.Resampling.LANCZOS)

    # Compress with fixed quality
    output = io.BytesIO()
    image.save(output, format='JPEG', quality=85, optimize=True)
    output.seek(0)
    return output.getvalue()

def image_to_base64(image_bytes: bytes) -> str:
    """Convert image bytes to base64 data URL."""
    base64_string = base64.b64encode(image_bytes).decode('utf-8')
    return f"data:image/jpeg;base64,{base64_string}"

def analyze_food_image(image: Image.Image) -> Optional[str]:
    """Analyze food image using OpenRouter API to identify dangerous ingredients."""
    try:
        # Process image
        with st.spinner("🔍 Processing image..."):
            processed_image_bytes = resize_and_compress_image(image)

        # Convert to base64
        base64_image = image_to_base64(processed_image_bytes)

        # Prepare API request
        api_key = get_api_key()
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": os.getenv('HTTP_REFERER', ''),
            "X-Title": os.getenv('X_TITLE', 'Food Safety Analyzer')
        }

        prompt = """Analyze this food image for safety concerns. Check for:
- Potentially harmful or unsafe ingredients

Provide a concise response about any dangerous ingredients or safety issues found."""

        payload = {
            "model": "google/gemini-2.5-flash-image-preview:free",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": base64_image
                            }
                        }
                    ]
                }
            ],
            "temperature": 0.1,
            "max_tokens": 1000
        }

        # Make API request with longer timeout
        with st.spinner("🧠 Analyzing ingredients..."):
            response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload, timeout=60)

        if response.status_code == 200:
            result = response.json()
            analysis = result['choices'][0]['message']['content']
            return analysis
        else:
            st.error(f"❌ API Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        st.error(f"❌ Error analyzing image: {str(e)}")
        return None

def format_analysis_result(analysis: str) -> str:
    """Format the analysis result for better display."""
    return analysis  # Keep it simple and clean

def main():
    st.title("🍎 Food Safety Analyzer")

    # Compact upload section
    col1, col2 = st.columns(2)

    uploaded_file = None
    camera_image = None

    with col1:
        st.markdown("📁 Upload Image")
        uploaded_file = st.file_uploader("Upload food image", type=SUPPORTED_FORMATS, label_visibility="collapsed")

    with col2:
        st.markdown("📸 Take Photo")
        camera_image = st.camera_input("Take photo of food", label_visibility="collapsed")

    # Auto-analyze when image is selected
    selected_image = None
    if uploaded_file:
        try:
            selected_image = Image.open(uploaded_file)
            st.success("✅ Image loaded")
        except:
            st.error("❌ Error loading image")
            return

    elif camera_image:
        try:
            selected_image = Image.open(camera_image)
            st.success("✅ Photo captured")
        except:
            st.error("❌ Error processing photo")
            return

    if selected_image:
        # Show compact preview
        st.image(selected_image, width=300)

        # Auto-analyze immediately
        with st.spinner("🔍 Analyzing..."):
            result = analyze_food_image(selected_image)

        if result:
            st.markdown("### 🏥 Analysis Results")
            st.markdown(f'<div class="result-section">{result}</div>', unsafe_allow_html=True)
        else:
            st.error("❌ Analysis failed. Please try again.")

    # Compact footer
    st.markdown("---")
    st.caption("🍎 Always consult healthcare professionals for medical advice")

if __name__ == "__main__":
    main()
