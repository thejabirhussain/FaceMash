from flask import Flask, request, jsonify
import cv2
import numpy as np
from werkzeug.utils import secure_filename
from facenet_model import compute_similarity  # Import FaceNet similarity function

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(file_storage):
    """Read image from memory and resize it."""
    try:
        # Convert file to NumPy array and read as image
        file_bytes = np.frombuffer(file_storage.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is None:
            return None  # Failed to read image

        img = cv2.resize(img, (160, 160))  # Resize for FaceNet
        return img
    except Exception as e:
        print(f"Error in preprocess_image: {e}")
        return None

@app.route("/", methods=["POST"])
def check_compatibility():
    if "file1" not in request.files or "file2" not in request.files:
        return jsonify({"error": "Missing files"}), 400

    file1 = request.files["file1"]
    file2 = request.files["file2"]

    if file1.filename == "" or file2.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
        img1 = preprocess_image(file1)
        img2 = preprocess_image(file2)

        if img1 is None or img2 is None:
            return jsonify({"error": "Image processing failed"}), 500

        score = compute_similarity(img1, img2)
        if score is None:
            return jsonify({"error": "Failed to compute compatibility"}), 500

        return jsonify({"compatibility_score": score})

    return jsonify({"error": "Invalid file format"}), 400

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
