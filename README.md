# 🍎 Food Safety Analyzer

A modern, AI-powered Streamlit application that analyzes food images to identify potentially dangerous ingredients and safety concerns using advanced vision language models.

## 🚀 Features

- **📁 Image Upload**: Upload food images from your device
- **📸 Camera Capture**: Take photos directly using your camera (mobile-friendly)
- **🧠 AI Analysis**: Powered by Google Gemini 2.0 Flash via OpenRouter API
- **🔍 Ingredient Detection**: Identifies common allergens and harmful ingredients
- **📱 Mobile Responsive**: Works seamlessly on desktop and mobile devices
- **⚡ Fast Processing**: Automatic image compression and optimization
- **🎨 Modern UI**: Clean, minimalist design with smooth animations

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Vision**: OpenRouter API (Google Gemini 2.0 Flash)
- **Image Processing**: Pillow (PIL)
- **Environment**: Python 3.8+
- **Deployment**: Streamlit Community Cloud

## 📋 Prerequisites

- Python 3.8 or higher
- OpenRouter API key ([Get one here](https://openrouter.ai/))
- Internet connection for API calls

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd food-safety-analyzer

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

Make sure your `.env` file contains:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
HTTP_REFERER=https://your-app-name.streamlit.app
X_TITLE=Food Safety Analyzer
```

### 3. Run Locally

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🌐 Deployment to Streamlit Community Cloud

### 1. Prepare Your Repository

Ensure your repository contains:
- `app.py` (main application)
- `requirements.txt` (dependencies)
- `.env` (API keys - will be configured in Streamlit Cloud)

### 2. Deploy on Streamlit Cloud

1. Go to [Streamlit Community Cloud](https://streamlit.io/cloud)
2. Connect your GitHub repository
3. Set the main file path to `app.py`
4. Add your secrets in the Streamlit Cloud dashboard:

   ```
   OPENROUTER_API_KEY = "your_openrouter_api_key_here"
   HTTP_REFERER = "https://your-app-name.streamlit.app"
   X_TITLE = "Food Safety Analyzer"
   ```

5. Click "Deploy"

## 📱 How to Use

1. **Upload Image**: Click "Choose an image file" to upload a food photo from your device
2. **Take Photo**: Use "Take a photo" to capture an image using your camera
3. **Analyze**: Click the "🔍 Analyze Food Safety" button
4. **Review Results**: Read the AI-generated analysis for potential safety concerns
5. **Download**: Save the analysis results as a text file

## 🎯 What It Detects

The AI analyzes images for:
- **Common Allergens**: Nuts, dairy, eggs, soy, wheat, fish, shellfish, peanuts
- **Harmful Ingredients**: Potentially dangerous additives or preservatives
- **Food Safety Issues**: Signs of spoilage, contamination, or expiration
- **Health Concerns**: Ingredients that may pose health risks

## 🔧 Configuration

### Image Processing
- **Maximum Size**: 20MB (automatically compressed)
- **Supported Formats**: PNG, JPG, JPEG, WebP, GIF
- **Quality Optimization**: Automatic quality adjustment for API compatibility

### AI Model Settings
- **Model**: Google Gemini 2.0 Flash
- **Temperature**: 0.1 (for consistent analysis)
- **Max Tokens**: 1000 (comprehensive but concise responses)

## 🛡️ Security & Privacy

- Images are processed locally before sending to the API
- No images are stored permanently on servers
- API keys are kept secure in environment variables
- All processing happens through secure HTTPS connections

## 🐛 Troubleshooting

### Common Issues

**API Key Error**
```
❌ OpenRouter API key not found
```
- Check your `.env` file exists and contains the correct API key
- Ensure the key starts with `sk-or-v1-`

**Image Upload Issues**
- Ensure image format is supported (PNG, JPG, JPEG, WebP, GIF)
- Check image size is under 50MB initially (will be compressed)

**Camera Not Working**
- Grant camera permissions in your browser
- Try refreshing the page
- Use a different browser if issues persist

### Performance Tips

- **Image Size**: Larger images take longer to process
- **Network**: Ensure stable internet connection for API calls
- **Browser**: Use modern browsers (Chrome, Firefox, Safari, Edge)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenRouter** for providing access to advanced AI models
- **Google** for the Gemini vision model
- **Streamlit** for the amazing web app framework
- **Pillow** for image processing capabilities

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Review the OpenRouter documentation

---

**⚠️ Disclaimer**: This application is for informational purposes only and should not replace professional medical advice. Always consult healthcare professionals for dietary concerns and allergies.
