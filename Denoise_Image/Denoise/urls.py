from django.urls import path
from . import views
app_name = 'Denoise'
urlpatterns = [
    path('', views.denoise_image, name='denoise_image'),
]
