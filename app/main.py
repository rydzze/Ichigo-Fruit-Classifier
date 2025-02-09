import os
import cv2
import numpy as np
from flask import current_app
from PIL import Image, ImageEnhance
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
model = load_model('app/model.h5', custom_objects={'preprocess_input': preprocess_input})

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def classify_image(image_path):
    img = image.load_img(image_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)
    probas = preds[0]

    max_proba = np.max(probas)
    if max_proba < 0.5:
        return 'Unknown', 'Unknown', 0
    class_idx = np.argmax(preds[0])
    
    labels = ['FreshApple', 'FreshBanana', 'FreshGrape', 'FreshGuava', 'FreshJujube', 'FreshOrange', 'FreshPomegranate', 'FreshStrawberry',
              'RottenApple', 'RottenBanana', 'RottenGrape', 'RottenGuava', 'RottenJujube', 'RottenOrange', 'RottenPomegranate', 'RottenStrawberry']
    fruit = labels[class_idx]
    
    if "Fresh" in fruit:
        fruit = fruit.replace("Fresh", "")
        condition = "Fresh"
    else:
        fruit = fruit.replace("Rotten", "")
        condition = "Rotten"

    return fruit, condition, 1

def enhance_image(image):
    img = Image.fromarray(image)
    
    brightness = ImageEnhance.Brightness(img)
    img_enhanced = brightness.enhance(1.1)
    
    saturation = ImageEnhance.Color(img_enhanced)
    img_enhanced = saturation.enhance(1.1)
    
    contrast = ImageEnhance.Contrast(img_enhanced)
    img_enhanced = contrast.enhance(1.1)
    
    return np.array(img_enhanced)

def sharpen_image(image):
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    laplacian_norm = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
    
    sharpened = cv2.addWeighted(image, 0.8, -laplacian_norm.astype(np.uint8), 0.2, 0)
    img_sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)
    
    return img_sharpened

def apply_canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 150, 250)
    kernel = np.ones((5, 5), np.uint8)
    
    return cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

def draw_bounding_boxes(image, edges, min_area=400, max_area=40000):
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_with_boxes = image.copy()
    number_of_fruit = 0
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= min_area and area <= max_area:
            number_of_fruit += 1
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image_with_boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return image_with_boxes, number_of_fruit

def process_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (256, 256))
    
    img_processed = enhance_image(img)
    img_processed = sharpen_image(img_processed)
    
    edges = apply_canny(img_processed)
    processed_img, number_of_fruit = draw_bounding_boxes(img, edges)
    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2RGB)
    
    processed_filename = f"processed_{os.path.basename(image_path)}"
    processed_path = os.path.join(current_app.config['UPLOAD_FOLDER'], processed_filename)
    cv2.imwrite(processed_path, processed_img)
    
    return processed_filename, number_of_fruit