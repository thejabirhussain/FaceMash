from flask import Flask, render_template, request, jsonify
import os
import cv2
import numpy as np
from model.facenet_model import compute_similarity  # Import AI model logic

# Force CPU usage (fix CUDA errors)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Initialize Flask app
app = Flask(__name__)

# Ensure 'uploads' folder exists
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "image1" not in request.files or "image2" not in request.files:
        return jsonify({"error": "Please upload two images!"})

    image1 = request.files["image1"]
    image2 = request.files["image2"]

    img1_path = os.path.join(app.config["UPLOAD_FOLDER"], image1.filename)
    img2_path = os.path.join(app.config["UPLOAD_FOLDER"], image2.filename)
    
    image1.save(img1_path)
    image2.save(img2_path)

    try:
        compatibility_score = compute_similarity(img1_path, img2_path)
        message = f"💖 Compatibility Score: {compatibility_score:.2f}% 💕"
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": "Error processing images!", "details": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Ensure correct port binding
    app.run(host="0.0.0.0", port=port, debug=True)
