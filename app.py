<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FaceMash AI - Love Compatibility</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            text-align: center;
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
            color: white;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 500px;
            background: white;
            color: #333;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
            margin: auto;
            animation: fadeIn 1s ease-in-out;
        }
        h1 {
            color: #ff3366;
        }
        input {
            display: block;
            margin: 10px auto;
            padding: 8px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            background: #ff3366;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
            transition: transform 0.2s ease-in-out;
        }
        button:hover {
            background: #cc2855;
            transform: scale(1.05);
        }
        #result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            transition: opacity 0.5s ease-in-out;
        }
        .preview {
            margin-top: 10px;
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .preview img {
            width: 100px;
            height: 100px;
            object-fit: cover;
            border-radius: 10px;
            border: 2px solid #ff3366;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.9); }
            to { opacity: 1; transform: scale(1); }
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>FaceMash AI ❤️</h1>
        <p>Upload photos of a couple & see their AI-calculated love compatibility! 💕</p>
        <form id="uploadForm">
            <label>Upload Partner 1 Photo:</label>
            <input type="file" id="image1" required>
            <label>Upload Partner 2 Photo:</label>
            <input type="file" id="image2" required>
            <div class="preview" id="previewContainer"></div>
            <button type="submit">Check Compatibility 🔍</button>
        </form>
        <div id="result">Waiting for input...</div>
         <p>Made by Batzz ❤️</p>
    </div>
        
    <script>
        function previewImage(input, previewId) {
            const file = input.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    let imgElement = document.getElementById(previewId);
                    if (!imgElement) {
                        imgElement = document.createElement("img");
                        imgElement.id = previewId;
                        document.getElementById("previewContainer").appendChild(imgElement);
                    }
                    imgElement.src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        }

        document.getElementById("image1").addEventListener("change", function () {
            previewImage(this, "preview1");
        });

        document.getElementById("image2").addEventListener("change", function () {
            previewImage(this, "preview2");
        });

        document.getElementById("uploadForm").addEventListener("submit", function(event) {
            event.preventDefault();

            let formData = new FormData();
            formData.append("file1", document.getElementById("image1").files[0]);
            formData.append("file2", document.getElementById("image2").files[0]);

            let resultDiv = document.getElementById("result");
            resultDiv.style.opacity = "0.5";
            resultDiv.innerHTML = "Analyzing... 🔍";

            fetch("/", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    resultDiv.innerHTML = `❌ ${data.error}`;
                } else if (data.message) {
                    resultDiv.innerHTML = `⚠️ ${data.message}`;
                } else {
                    resultDiv.innerHTML = `💖 Compatibility Score: <b>${data.compatibility_score}%</b>`;
                }
                resultDiv.style.opacity = "1";
            })
            .catch(error => {
                console.error("Error:", error);
                resultDiv.innerHTML = "❌ Error processing images!";
            });
        });
    </script>

</body>
</html>
