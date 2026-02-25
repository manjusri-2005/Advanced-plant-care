from flask import Flask, render_template, request
from config import Config
from utils.predict import predict_disease
from utils.image_helper import save_uploaded_image
import ospyth

# ===== APP INITIALIZATION =====
app = Flask(__name__)
app.config.from_object(Config)

UPLOAD_FOLDER = app.config["UPLOAD_FOLDER"]

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ===== ROUTES =====

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict")
def predict_page():
    return render_template("predict.html")


@app.route("/result", methods=["POST"])
def result():
    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    image_path = save_uploaded_image(file, UPLOAD_FOLDER)

    prediction, confidence = predict_disease(image_path)

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence,
        image_path=image_path
    )


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)