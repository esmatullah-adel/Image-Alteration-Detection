import os
import numpy as np
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load the model only once
MODEL_PATH = os.path.join(settings.BASE_DIR, 'model/mobilenetv2_model.h5')
model = load_model(MODEL_PATH)

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)[0][0]
    return "Real" if prediction < 0.5 else "Fake"

def main(request):
    result = None
    image_url = None

    if request.method == 'POST' and request.FILES.get('image'):
        img_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(img_file.name, img_file)
        file_path = fs.path(filename)
        image_url = fs.url(filename)

        result = predict_image(file_path)

    return render(request, 'main.html', {
        'result': result, 
        'image_url': image_url
        })
