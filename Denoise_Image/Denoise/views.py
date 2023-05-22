

# import cv2
# import base64
# from django.shortcuts import render
# import numpy as np

# def denoise_image(request):
#     if request.method == 'POST':
#         image = request.FILES['image']
        
#         # Read and denoise the image
#         img_array = np.frombuffer(image.read(), np.uint8)
#         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#         denoised_image = cv2.fastNlMeansDenoisingColored(img, None, 6, 3, 7, 30)
        
#         # Encode the denoised image as base64
#         _, buffer = cv2.imencode('.jpeg', denoised_image)
#         denoised_image_base64 = base64.b64encode(buffer).decode('utf-8')
        
#         return render(request, 'denoise_result.html', {'denoised_image': denoised_image_base64})

#     return render(request, 'denoise.html')


  
import cv2
import base64
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ImageForm
from .models import Image
import numpy as np

def denoise_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            # Read and denoise the image
            img_array = np.frombuffer(image.image.read(), np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            denoised_image = cv2.fastNlMeansDenoisingColored(img, None, 6, 3, 7, 30)
            
            # Encode the denoised image as base64
            _, buffer = cv2.imencode('.jpeg', denoised_image)
            denoised_image_base64 = base64.b64encode(buffer).decode('utf-8')
            
            return render(request, 'denoise_result.html', {'denoised_image': denoised_image_base64})
    else:
        form = ImageForm()
    
    images = Image.objects.all()
    return render(request, 'denoise.html', {'form': form, 'images': images})



def image_list(request):
    images = Image.objects.all()
    return render(request, 'image_list.html', {'images': images})

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'image_detail.html', {'image': image})

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})

def image_update(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('image_detail', pk=pk)
    else:
        form = ImageForm(instance=image)
    return render(request, 'image_update.html', {'form': form})

def image_delete(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        image.delete()
        return redirect('image_list')
    return render(request, 'image_delete.html', {'image': image})