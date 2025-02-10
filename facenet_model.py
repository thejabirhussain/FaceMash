import cv2
import numpy as np
from keras_facenet import FaceNet

embedder = FaceNet()

def compute_similarity(img1, img2):
    try:
        # Convert images to RGB
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        # Normalize images
        img1 = img1.astype("float32") / 255.0
        img2 = img2.astype("float32") / 255.0

        # Get embeddings
        embeddings = embedder.embeddings([img1, img2])
        emb1, emb2 = embeddings[0], embeddings[1]

        # Compute cosine similarity
        cosine_similarity = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))

        # Compute Euclidean distance
        euclidean_distance = np.linalg.norm(emb1 - emb2)

        # Scale similarity percentage
        similarity_percentage = round((cosine_similarity + 1) * 45 + np.random.uniform(-5, 5), 2)
        similarity_percentage = min(similarity_percentage, 98.5)  # Ensure it never reaches 100%

        return similarity_percentage
    except Exception as e:
        print("Error:", str(e))
        return None
