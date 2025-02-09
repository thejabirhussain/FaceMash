from flask import Flask, request, render_template, jsonify
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    """Resize image to reduce memory usage."""
    img = cv2.imread(image_path)
    if img is None:
        return None
    img = cv2.resize(img, (160, 160))  # Resize for faster processing
    cv2.imwrite(image_path, img)
    return image_path

def compute_similarity(img1_path, img2_path):
    """Dummy function to simulate AI model for compatibility check."""
    try:
        img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

        if img1 is None or img2 is None:
            return None  # Image processing failed

        hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
        similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

        return round(similarity * 100, 2)  # Convert to percentage
    except Exception as e:
        print(f"Error in compute_similarity: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file1" not in request.files or "file2" not in request.files:
            return jsonify({"error": "Missing files"}), 400

        file1 = request.files["file1"]
        file2 = request.files["file2"]

        if file1.filename == "" or file2.filename == "":
            return jsonify({"error": "No selected file"}), 400

        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)

            path1 = os.path.join(app.config["UPLOAD_FOLDER"], filename1)
            path2 = os.path.join(app.config["UPLOAD_FOLDER"], filename2)

            file1.save(path1)
            file2.save(path2)

            # Resize images
            path1 = preprocess_image(path1)
            path2 = preprocess_image(path2)

            if path1 is None or path2 is None:
                return jsonify({"error": "Image processing failed"}), 500

            score = compute_similarity(path1, path2)
            if score is None:
                return jsonify({"error": "Failed to compute compatibility"}), 500

            return jsonify({"compatibility_score": score})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
