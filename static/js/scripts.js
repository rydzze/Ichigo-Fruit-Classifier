function validateFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const allowedTypes = ['image/jpeg', 'image/png', 'image/jpg'];

    if (file && !allowedTypes.includes(file.type)) {
        alert('Only image files (png, jpg, jpeg) are allowed.');
        fileInput.value = '';
    }
}