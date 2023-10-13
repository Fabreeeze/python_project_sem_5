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
        console.log("data sent"); 
        console.log(result);

        if (result.success) {
            const successMessage = document.createElement('div');
            successMessage.classList.add('alert', 'alert-success', 'mt-4','fixed-top', 'text-center', 'w-100');
            successMessage.innerText = 'Image successfully scanned and uploaded!';
            document.body.appendChild(successMessage);

            // Set a timeout to remove the success message after 3 seconds
            setTimeout(function() {
                successMessage.remove();
            }, 5000);

            const imagePreview = document.querySelector('.image-preview');
            if (imagePreview) {
                imagePreview.remove();
            }

        } 
        else {
            console.log("here ===== "+response);
            console.error('Error uploading image');
        }
    });
});
