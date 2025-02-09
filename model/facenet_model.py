import cv2
import numpy as np
from keras_facenet import FaceNet

# Initialize FaceNet model
embedder = FaceNet()

# Store last checked image paths
last_checked_images = None  

def compute_similarity(image1_path, image2_path):
    global last_checked_images

    try:
        # Prevent rechecking if images haven't changed
        if last_checked_images == (image1_path, image2_path):
            return "Please change the images before checking compatibility again."

        # Read images
        img1 = cv2.imread(image1_path)
        img2 = cv2.imread(image2_path)

        if img1 is None or img2 is None:
            raise ValueError("Error: One or both images could not be read.")

        # Convert images to RGB
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

        # Resize to FaceNet input size
        img1 = cv2.resize(img1, (160, 160))
        img2 = cv2.resize(img2, (160, 160))

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

        # Scale similarity to avoid 100% matches
        similarity_percentage = round((cosine_similarity + 1) * 45 + np.random.uniform(-5, 5), 2)

        # Ensure it's never exactly 100%
        similarity_percentage = min(similarity_percentage, 98.5)

        # Save last checked images
        last_checked_images = (image1_path, image2_path)

        # Debugging
        print("Cosine Similarity:", cosine_similarity)
        print("Euclidean Distance:", euclidean_distance)
        print("Final Similarity Percentage:", similarity_percentage)

        return similarity_percentage

    except Exception as e:
        print("Error:", str(e))
        return 0  # Return 0% in case of an error
