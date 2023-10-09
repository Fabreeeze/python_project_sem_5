document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);

    fetch('/process_image', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);

        if (data.success) {
            const successMessage = document.createElement('div');
            successMessage.classList.add('success-message');
            successMessage.innerText = 'Image successfully scanned and uploaded!';
            document.body.appendChild(successMessage);

            // Set a timeout to remove the success message after 3 seconds
            setTimeout(function() {
                successMessage.remove();
            }, 7000);

            const imagePreview = document.querySelector('.image-preview');
            if (imagePreview) {
                imagePreview.remove();
            }

        } else {
            console.error('Error uploading image');
        }

    })
    .catch(error => console.error('Error:', error));

});
