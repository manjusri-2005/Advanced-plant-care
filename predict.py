import numpy as np
import json
import os

# prefer tensorflow.keras but fall back to standalone keras if necessary
try:
    import tensorflow as tf
    load_model = tf.keras.models.load_model
except Exception:
    from keras.models import load_model

from utils.preprocess import preprocess_image

# Load model if available
MODEL_PATH = "models/plant_disease_model.h5"
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = tensorflow.keras.models.load_model(MODEL_PATH)
    except Exception:
        model = None

# Load class labels
with open("models/class_labels.json", "r") as f:
    class_labels = json.load(f)

def predict_disease(img_path):
    if model is None:
        raise RuntimeError("Model not loaded; ensure models/plant_disease_model.h5 exists and is a valid model.")
    processed_image = preprocess_image(img_path)
    prediction = model.predict(processed_image)
    predicted_class = class_labels[int(np.argmax(prediction))]
    confidence = float(np.max(prediction)) * 100
    return predicted_class, round(confidence, 2)