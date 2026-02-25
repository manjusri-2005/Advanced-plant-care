console.log("Plant Disease Detection App Loaded");

function showPreview(event) {
    const image = document.getElementById("preview");
    image.src = URL.createObjectURL(event.target.files[0]);
    image.style.display = "block";
}