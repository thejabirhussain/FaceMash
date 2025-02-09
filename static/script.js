document.getElementById("uploadForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let formData = new FormData();
    formData.append("image1", document.getElementById("image1").files[0]);
    formData.append("image2", document.getElementById("image2").files[0]);

    let resultDiv = document.getElementById("result");
    resultDiv.style.opacity = "0.5";
    resultDiv.innerHTML = "Analyzing... 🔍";

    fetch("/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = data.message;
        resultDiv.style.opacity = "1";
    })
    .catch(error => {
        console.error("Error:", error);
        resultDiv.innerHTML = "Error processing images!";
    });
});
