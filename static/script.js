document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const response = await fetch('/process_image', {
            method: 'POST',
            body: formData,
        });
        const result = await response.json();
        document.getElementById('result').innerHTML = result.message;
    });
});
