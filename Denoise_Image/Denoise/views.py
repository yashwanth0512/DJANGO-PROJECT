

import cv2
import base64
from django.shortcuts import render
import numpy as np

def denoise_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        
        # Read and denoise the image
        img_array = np.frombuffer(image.read(), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        denoised_image = cv2.fastNlMeansDenoisingColored(img, None, 6, 3, 7, 30)
        
        # Encode the denoised image as base64
        _, buffer = cv2.imencode('.jpeg', denoised_image)
        denoised_image_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return render(request, 'denoise_result.html', {'denoised_image': denoised_image_base64})

    return render(request, 'denoise.html')

# def index(request) :
#     return render(request, 'index.html')    
  
