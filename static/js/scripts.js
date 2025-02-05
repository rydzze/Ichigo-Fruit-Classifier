document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    
    dropZone.addEventListener('click', () => fileInput.click());

    ['dragover', 'dragleave', 'drop'].forEach(event => {
        dropZone.addEventListener(event, preventDefaults);
    });

    ['dragover', 'dragenter'].forEach(event => {
        dropZone.addEventListener(event, highlight);
    });

    ['dragleave', 'drop'].forEach(event => {
        dropZone.addEventListener(event, unhighlight);
    });

    dropZone.addEventListener('drop', handleDrop);

    fileInput.addEventListener('change', handleFileSelect);
});

function preventDefaults (e) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight() {
    document.getElementById('dropZone').classList.add('dragover');
}

function unhighlight() {
    document.getElementById('dropZone').classList.remove('dragover');
}

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    
    if (files.length > 0) {
        fileInput.files = files;
        handleFileSelect();
    }
}

function handleFileSelect() {
    const file = fileInput.files[0];
    const allowedTypes = ['image/jpeg', 'image/png', 'image/jpg'];

    if (file && !allowedTypes.includes(file.type)) {
        alert('Only image files (png, jpg, jpeg) are allowed.');
        fileInput.value = '';
        return;
    }

    if (file) {
        showLoading();
        setTimeout(() => {
            document.querySelector('form').submit();
        }, 1500);
    }
}

function showLoading() {
    document.getElementById('loadingOverlay').style.display = 'flex';
}