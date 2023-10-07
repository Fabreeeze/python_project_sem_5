function showUploadTab() {
    document.getElementById('uploadTab').style.display = 'block';
    document.getElementById('databaseTab').style.display = 'none';
}

function showDatabaseTab() {
    document.getElementById('uploadTab').style.display = 'none';
    document.getElementById('databaseTab').style.display = 'block';
}



document.getElementById('imageUpload').addEventListener('change', function(event) {
    const previewImage = document.getElementById('previewImage');
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function() {
        previewImage.src = reader.result;
    };

    reader.readAsDataURL(file);

    const removeIcon = document.getElementById("remove_icon");
    removeIcon.style.display = 'block';
});

function removeImage() {
    const previewImage = document.getElementById('previewImage');
    previewImage.src = "#";

    const removeIcon = document.getElementById("remove_icon");
    removeIcon.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData,
        });
        const result = await response.json();
        document.getElementById('result').innerHTML = result.message;
    });
});
