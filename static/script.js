function switchTab(tabId) {

    // Hide all tab contents and deactivate all tabs
    document.querySelectorAll('.tabContent').forEach(content => content.style.display = 'none');
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));

    // Show the selected tab content and activate the selected tab
    document.getElementById(tabId).style.display = 'block';
    document.getElementById(tabId).classList.add('active');
}

switchTab('uploadDiv');


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
