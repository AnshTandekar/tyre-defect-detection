# 🚗 AI-Powered Tyre Defect Detection System

Advanced quality control system using Convolutional Neural Networks (CNN) to detect defective tyres with **95.5% accuracy**.

**🔗 Live Web App:** https://tyre-defect-detection.onrender.com  
Detect tyre defects using a CNN-based deep learning model. 


![Python](https://img.shields.io/badge/Python-3.12-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19.0-orange)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green)

## 🎯 Project Overview

This AI system automatically identifies defects in tyre images using deep learning. Perfect for manufacturing quality control, inspection automation, and safety verification.

### ✨ Key Features

- 🎯 **High Accuracy**: 95.45% validation accuracy, 94.74% precision, 97.75% recall
- ⚡ **Real-time Detection**: Results in under 1 second
- 🎨 **Interactive UI**: Beautiful drag-and-drop interface
- 📊 **Detailed Analysis**: Confidence scores and safety recommendations
- 🔒 **Production-Ready**: Docker containerized for easy deployment
- 📱 **Responsive Design**: Works on desktop, tablet, and mobile

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| **Validation Accuracy** | 95.45% |
| **Precision** | 94.74% |
| **Recall** | 97.75% |
| **Test Accuracy** | 95.00% |
| **Dataset Size** | 1,856 images |
| **Classes** | 2 (Defective, Good) |

## 🏗️ Model Architecture

```
Input (300×300×3 RGB Image)
         ↓
Conv2D (128 filters) → BatchNorm → MaxPool
         ↓
Conv2D (128 filters) → BatchNorm → MaxPool
         ↓
Conv2D (128 filters) → BatchNorm → MaxPool
         ↓
Flatten → Dense (64) → Dropout (0.5)
         ↓
Dense (1, Sigmoid) → Binary Classification
         ↓
Output: Defective (0) or Good (1)
```

### Training Details
- **Optimizer**: SGD
- **Loss Function**: Binary Crossentropy
- **Regularization**: Dropout (0.5) + Batch Normalization
- **Callbacks**: Early Stopping (patience=8), Model Checkpoint
- **Best Model**: Epoch 30 with 95.45% validation accuracy

## 🚀 Quick Start

### Prerequisites
- Python 3.12
- pip
- (Optional) Docker

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/tyre-defect-detection.git
cd tyre-defect-detection
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your trained model**
Place your `tyre_model.keras` file in the project root directory.

5. **Run the application**
```bash
python app.py
```

6. **Open in browser**
Navigate to `http://localhost:5000`

### Docker Installation

1. **Build Docker image**
```bash
docker build -t tyre-detector .
```

2. **Run container**
```bash
docker run -p 5000:5000 tyre-detector
```

3. **Access application**
Open `http://localhost:5000` in your browser

## 📁 Project Structure

```
tyre-defect-detection/
│
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── tyre_model.keras         # Trained model (add this)
│
├── templates/
│   └── index.html           # Web interface
│
├── .gitignore               # Git ignore rules
└── README.md                # Documentation
```

## 🎨 User Interface Features

- **Drag & Drop Upload**: Simply drag images onto the upload area
- **Real-time Preview**: See your image before analysis
- **Animated Results**: Smooth transitions and visual feedback
- **Color-Coded Status**: Green for good tyres, red for defective
- **Confidence Meter**: Visual bar showing prediction confidence
- **Safety Levels**: Critical, High Risk, Moderate Risk, Safe, Acceptable
- **Smart Recommendations**: Actionable advice based on detection results
- **Mobile Responsive**: Perfect on all screen sizes

## 📖 API Documentation

### Endpoint: Predict Tyre Condition

**URL:** `/predict`  
**Method:** `POST`  
**Content-Type:** `multipart/form-data`

**Request:**
```bash
curl -X POST -F "image=@tyre_image.jpg" http://localhost:5000/predict
```

**Success Response (200):**
```json
{
  "success": true,
  "data": {
    "class_name": "Good Tyre",
    "class_index": 1,
    "confidence": 96.32,
    "raw_prediction": 0.9632,
    "is_defective": false,
    "is_safe": true,
    "safety_level": "SAFE",
    "recommendation": "✅ EXCELLENT: Tyre is in very good condition...",
    "image_data": "base64_encoded_image"
  }
}
```

**Error Response (400/500):**
```json
{
  "success": false,
  "error": "Error message here"
}
```

### Other Endpoints

**Health Check:** `GET /health`
```json
{
  "status": "healthy",
  "model_status": "loaded",
  "image_size": [300, 300]
}
```

**Model Info:** `GET /model-info`
```json
{
  "model_name": "Tyre Defect Detection CNN",
  "input_shape": [300, 300, 3],
  "classes": ["Defective Tyre", "Good Tyre"],
  "architecture": "3 Conv Blocks + 2 Dense Layers",
  "metrics": {
    "validation_accuracy": "95.45%",
    "precision": "94.74%",
    "recall": "97.75%"
  }
}
```

## 🌐 Deployment Guide

### Deploy to Render (Free)

1. **Push to GitHub**
   - Create a new repository
   - Upload all files including `tyre_model.keras`
   - Use Git LFS if model > 100MB

2. **Create Web Service on Render**
   - Go to [render.com](https://render.com)
   - Sign up/login with GitHub
   - Click "New +" → "Web Service"
   - Connect your repository

3. **Configure Service**
   - **Name**: `tyre-defect-detection`
   - **Runtime**: `Docker` ⚠️ Important!
   - **Plan**: Free
   - Click "Create Web Service"

4. **Wait for deployment** (10-15 minutes)
   - Render will build Docker image
   - Deploy your application
   - Provide you with a live URL

### Deploy to Railway

1. Push code to GitHub
2. Go to [railway.app](https://railway.app)
3. Sign up with GitHub
4. Deploy from GitHub repo
5. Railway auto-detects Docker
6. Get deployment URL

## 🔧 Configuration

### Environment Variables
```bash
PORT=5000  # Port number (auto-set by hosting platforms)
```

### Model Configuration
Edit `app.py` to customize:
- Model path: `MODEL_PATH = 'tyre_model.keras'`
- Image size: `IMAGE_SIZE = (300, 300)`
- Max file size: `MAX_FILE_SIZE = 10 * 1024 * 1024`

## 🧪 Testing

### Test with Sample Images

1. **Prepare test images**
   - Defective tyres (cracks, bubbles, deformations)
   - Good tyres (normal condition)

2. **Upload via web interface**
   - Drag & drop or click to upload
   - Click "Analyze Tyre Condition"
   - View results with confidence scores

3. **Verify API endpoints**
```bash
# Health check
curl http://localhost:5000/health

# Model info
curl http://localhost:5000/model-info

# Prediction
curl -X POST -F "image=@test_tyre.jpg" http://localhost:5000/predict
```

## 🐛 Troubleshooting

### Common Issues

**Issue: Model not loading**
- ✅ Verify `tyre_model.keras` exists in project root
- ✅ Check file name matches exactly (case-sensitive)
- ✅ Ensure TensorFlow is installed: `pip list | grep tensorflow`

**Issue: "No image file provided" error**
- ✅ Check form data key is named 'image'
- ✅ Verify Content-Type is multipart/form-data
- ✅ Ensure file is actually selected

**Issue: Predictions seem wrong**
- ✅ Verify uploaded image is clear and well-lit
- ✅ Check image shows the tyre clearly
- ✅ Ensure preprocessing matches training (resize to 300×300)

**Issue: Docker build fails**
- ✅ Ensure Docker is running
- ✅ Check Dockerfile syntax
- ✅ Verify requirements.txt has correct versions

**Issue: Model file too large for GitHub**
```bash
# Install Git LFS
git lfs install

# Track large files
git lfs track "*.keras"
git add .gitattributes
git add tyre_model.keras
git commit -m "Add model with LFS"
git push
```

## 💡 How It Works

### Image Processing Pipeline

1. **Upload**: User uploads tyre image
2. **Validation**: Check file type and size
3. **Preprocessing**:
   - Convert to RGB
   - Resize to 300×300 pixels
   - Normalize pixels to [0, 1]
   - Add batch dimension
4. **Prediction**: CNN model analyzes image
5. **Interpretation**:
   - Sigmoid output → Class (0 or 1)
   - Calculate confidence percentage
   - Generate safety level
   - Create recommendation
6. **Response**: Return results with base64 image

### CNN Classification Process

```
Image → Feature Extraction (Conv Layers) → Pattern Recognition
         ↓
    Batch Normalization (Stabilize)
         ↓
    MaxPooling (Reduce Dimensions)
         ↓
    Flatten → Dense Layers → Dropout
         ↓
    Sigmoid Output (0.0 to 1.0)
         ↓
    Threshold at 0.5 → Binary Decision
```

## 📈 Future Enhancements

- [ ] Multi-class defect detection (cracks, bubbles, wear, deformation)
- [ ] Batch processing for multiple images
- [ ] Prediction history and analytics dashboard
- [ ] Export reports to PDF
- [ ] Real-time camera feed analysis
- [ ] Integration with manufacturing systems
- [ ] User authentication and roles
- [ ] Database storage for audit trails
- [ ] Email/SMS alerts for critical defects
- [ ] Mobile app (iOS/Android)

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Your Name**
- GitHub: [Ansh Tandekar](https://github.com/AnshTandekar)
- LinkedIn: [Ans Tandekar](https://www.linkedin.com/in/ansh-tandekar-b95315212/)
- Email: anshtandekar55@gmail.com

## 🙏 Acknowledgments

- Dataset: Digital images of defective and good condition tyres
- TensorFlow/Keras team for the deep learning framework
- Flask team for the lightweight web framework
- Render/Railway for free hosting platforms

## 📞 Support

Need help? Here's how to get support:

- 📧 **Email**: anshtandekar55@gmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/AnshTandekar/tyre-defect-detection/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/AnshTandekar/tyre-defect-detection/discussions)

## ⚖️ Legal & Safety Notice

**Important:** This system is designed for educational and demonstration purposes. For production use in critical safety applications:

- ✅ Additional validation and testing required
- ✅ Consult with domain experts and quality control professionals
- ✅ Regular model retraining with new data
- ✅ Human oversight for critical decisions
- ✅ Compliance with industry standards and regulations

**Disclaimer:** The predictions are probabilistic and should not be the sole basis for safety-critical decisions. Always combine AI analysis with professional human inspection.

---

⭐ **If you find this project helpful, please star the repository!**

Made with ❤️ using Python, TensorFlow, and Flask
