document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');

    // Click event to trigger file input when drop zone is clicked
    dropZone.addEventListener('click', () => fileInput.click());

    // Prevent default behaviors for drag events
    ['dragover', 'dragleave', 'drop'].forEach(event => {
        dropZone.addEventListener(event, preventDefaults);
    });

    // Highlight drop zone on dragover and dragenter
    ['dragover', 'dragenter'].forEach(event => {
        dropZone.addEventListener(event, highlight);
    });

    // Remove highlight on dragleave and drop
    ['dragleave', 'drop'].forEach(event => {
        dropZone.addEventListener(event, unhighlight);
    });

    // Handle file drop
    dropZone.addEventListener('drop', handleDrop);

    // Handle file selection via input
    fileInput.addEventListener('change', handleFileSelect);
});

/**
 * Prevents default drag-and-drop behaviors
 * @param {Event} e - The event object
 */
function preventDefaults(e){
    e.preventDefault();
    e.stopPropagation();
}

/**
 * Adds highlight effect to drop zone
 */
function highlight(){
    document.getElementById('dropZone').classList.add('dragover');
}

/**
 * Removes highlight effect from drop zone
 */
function unhighlight(){
    document.getElementById('dropZone').classList.remove('dragover');
}

/**
 * Handles file drop event
 * @param {DragEvent} e - The drag event object
 */
function handleDrop(e){
    const dt = e.dataTransfer;
    const files = dt.files;
    
    if(files.length > 0){
        fileInput.files = files;
        handleFileSelect();
    }
}

/**
 * Handles file selection event
 */
function handleFileSelect(){
    const file = fileInput.files[0];
    const allowedTypes = ['image/jpeg', 'image/png', 'image/jpg'];

    if(file && !allowedTypes.includes(file.type)){
        alert('Only image files (png, jpg, jpeg) are allowed.');
        fileInput.value = '';
        return;
    }

    if(file){
        showLoading();
        setTimeout(() => {
            document.querySelector('form').submit();
        }, 1000);
    }
}

/**
 * Displays a loading overlay
 */
function showLoading(){
    document.getElementById('loadingOverlay').style.display = 'flex';
}