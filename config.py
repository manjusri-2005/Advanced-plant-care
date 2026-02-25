import os

class Config:
    # Secret key for Flask (security purpose)
    SECRET_KEY = "supersecretkey"

    # Upload folder path
    UPLOAD_FOLDER = os.path.join("static", "uploads")

    # Allowed image extensions
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

    # Model path
    MODEL_PATH = os.path.join("models", "plant_disease_model.h5")

    # Image size for model input
    IMAGE_SIZE = (224, 224)