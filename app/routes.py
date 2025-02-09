import os
from werkzeug.utils import secure_filename
from app.main import allowed_file, classify_image, process_image
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_from_directory

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

@bp.route('/result', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename, current_app.config['ALLOWED_EXTENSIONS']):
        filename = secure_filename(file.filename)
    
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(file_path)

        fruit, condition, is_fruit = classify_image(file_path)

        if is_fruit == 0:
            return render_template('result.html', input_image=filename, fruit=fruit, condition=condition, count='-')
        
        img_with_box, count = process_image(file_path)
        return render_template('result.html', input_image=img_with_box, fruit=fruit, condition=condition, count=count)
    else:
        flash('Only image files are allowed (png, jpg, jpeg).')
        return redirect(url_for('routes.home'))