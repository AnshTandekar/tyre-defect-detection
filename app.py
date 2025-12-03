from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import io
import base64
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = 'tyre_model.keras'
model = None

def load_model_file():
    global model
    if os.path.exists(MODEL_PATH):
        model = keras.models.load_model(MODEL_PATH)
        print("✓ Model loaded successfully")
    else:
        print(f"⚠ Warning: Model file '{MODEL_PATH}' not found!")

# Load model at startup
load_model_file()

# Class names
CLASS_NAMES = ['Defective Tyre', 'Good Tyre']

def preprocess_image(image_file):
    """
    Preprocess uploaded image for prediction
    """
    # Open image
    img = Image.open(image_file)
    
    # Convert to RGB if necessary
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Resize to model input size
    img = img.resize((300, 300))
    
    # Convert to array and normalize
    img_array = np.array(img)
    img_array = img_array / 255.0
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array, img

def predict_tyre_condition(image_file):
    """
    Predict if tyre is defective or good
    """
    if model is None:
        return None, "Model not loaded"
    
    # Preprocess image
    processed_image, original_image = preprocess_image(image_file)
    
    # Make prediction
    prediction = model.predict(processed_image, verbose=0)[0][0]
    
    # Interpret results
    # prediction close to 0 = Defective, close to 1 = Good
    confidence = prediction if prediction > 0.5 else 1 - prediction
    predicted_class = 1 if prediction > 0.5 else 0
    class_name = CLASS_NAMES[predicted_class]
    
    # Convert image to base64 for display
    buffer = io.BytesIO()
    original_image.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode()
    
    return {
        'class': class_name,
        'class_index': int(predicted_class),
        'confidence': float(confidence * 100),
        'raw_prediction': float(prediction),
        'image_data': img_str,
        'is_defective': predicted_class == 0,
        'recommendation': get_recommendation(predicted_class, confidence)
    }

def get_recommendation(predicted_class, confidence):
    """
    Provide recommendation based on prediction
    """
    if predicted_class == 0:  # Defective
        if confidence > 0.9:
            return "⚠️ HIGH RISK: This tyre shows clear signs of defects. Replace immediately for safety."
        elif confidence > 0.7:
            return "⚠️ MODERATE RISK: Defects detected. Inspect the tyre and consider replacement."
        else:
            return "⚠️ POSSIBLE DEFECT: Some defects detected. Get a professional inspection."
    else:  # Good
        if confidence > 0.9:
            return "✅ EXCELLENT: Tyre appears to be in good condition. Safe for use."
        elif confidence > 0.7:
            return "✅ GOOD: Tyre is in acceptable condition. Monitor regularly."
        else:
            return "✅ FAIR: Tyre appears okay but have it checked during next service."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if image is in request
        if 'image' not in request.files:
            return jsonify({
                'success': False, 
                'error': 'No image file provided'
            }), 400
        
        file = request.files['image']
        
        # Check if file is empty
        if file.filename == '':
            return jsonify({
                'success': False, 
                'error': 'Empty filename'
            }), 400
        
        # Check file extension
        allowed_extensions = {'png', 'jpg', 'jpeg', 'bmp', 'gif'}
        file_ext = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ''
        
        if file_ext not in allowed_extensions:
            return jsonify({
                'success': False, 
                'error': f'Invalid file type. Allowed: {", ".join(allowed_extensions)}'
            }), 400
        
        # Make prediction
        result = predict_tyre_condition(file)
        
        if result is None:
            return jsonify({
                'success': False, 
                'error': 'Model not available'
            }), 500
        
        return jsonify({
            'success': True,
            'data': result
        })
    
    except Exception as e:
        return jsonify({
            'success': False, 
            'error': f'Prediction failed: {str(e)}'
        }), 500

@app.route('/health')
def health():
    model_status = 'loaded' if model is not None else 'not_loaded'
    return jsonify({
        'status': 'healthy',
        'model_status': model_status
    })

@app.route('/model-info')
def model_info():
    if model is None:
        return jsonify({
            'error': 'Model not loaded'
        }), 500
    
    return jsonify({
        'input_shape': [300, 300, 3],
        'classes': CLASS_NAMES,
        'accuracy': '95.45%',
        'precision': '94.74%',
        'recall': '97.75%'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)