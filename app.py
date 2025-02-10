from flask import Flask, request, render_template, jsonify
import os
import random
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
TEMP_FOLDER = "temp_uploads"  # Temporary folder for storing images (not in GitHub)
os.makedirs(TEMP_FOLDER, exist_ok=True)

last_uploaded_images = {}  # Store last uploaded image names
last_score = None  # Store last computed score

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_random_score():
    """Generates a random compatibility score between 60-95."""
    return random.randint(60, 95)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    global last_uploaded_images, last_score  # Access previous uploads

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

            path1 = os.path.join(TEMP_FOLDER, filename1)
            path2 = os.path.join(TEMP_FOLDER, filename2)

            file1.save(path1)
            file2.save(path2)

            # Check if the same images were uploaded again
            if last_uploaded_images.get("file1") == filename1 and last_uploaded_images.get("file2") == filename2:
                return jsonify({"message": "Please change images before re-uploading"}), 400

            # Generate a random score
            score = generate_random_score()

            # Store last uploaded images and score
            last_uploaded_images["file1"] = filename1
            last_uploaded_images["file2"] = filename2
            last_score = score

            return jsonify({"compatibility_score": score})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
