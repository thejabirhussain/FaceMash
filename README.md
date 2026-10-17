# FaceMash 😎💖

FaceMash is a fun web application that compares two people's faces and determines how compatible they are using deep learning facial recognition. Built using Python, Gradio, Flask, and powerful tools like TensorFlow, FaceNet, and OpenCV.

---

## 🚀 Features

* Upload two face images
* Get a compatibility score between 0% and 100%
* Deep learning-based facial feature extraction using FaceNet
* Web interface using Gradio
* Backend served via Flask + Gunicorn

---

## 🧠 Tech Stack

* **Python** – Main programming language
* **Flask** – Web server & routing
* **Gradio** – UI for image input and result display
* **OpenCV** – Image processing
* **Keras-FaceNet** – Deep facial feature embeddings
* **TensorFlow** – Backbone for model computations
* **NumPy** – Numerical operations
* **SciPy** – Cosine similarity & distance metrics
* **Gunicorn** – Production WSGI HTTP server
* **Werkzeug** – WSGI utilities

---

## 📦 Installation

### Prerequisites

Make sure Python 3.7+ is installed.

```bash
git clone https://github.com/yourusername/facemash.git
cd facemash
```

### Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, you can use:

```bash
pip install flask gradio numpy opencv-python keras_facenet tensorflow scipy gunicorn werkzeug
```

---

## 🧪 How It Works

1. The user uploads two images via Gradio UI.
2. FaceNet extracts embeddings (128-dimension vector) for each face.
3. Cosine similarity is calculated between both vectors.
4. A compatibility score is generated based on similarity.

---

## ▶️ Running the App

### Development server (local):

```bash
python app.py
```

### Production (with Gunicorn):

```bash
gunicorn app:app
```

---

## 📁 Project Structure

```
facemash/
│
├── app.py               # Main Flask app
├── face_matcher.py      # Core logic to compare faces
├── templates/           # (If used) HTML templates for Flask
├── static/              # Static files like images/css (if needed)
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 📸 UI Snapshot

> ![Preview](preview.png)
> *Upload any two faces & find out your compatibility score instantly!*

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change or improve.

---

## 📄 License

Copyright (c) 2025-2026 Mohammed Jabir Hussain Shaik. All rights reserved. See [LICENSE](LICENSE).

---


Made by Jabir Hussain (https://github.com/thejabirhussain) — Let's match some faces!
