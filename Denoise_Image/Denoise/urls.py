from django.urls import path
from . import views
app_name = 'Denoise'
urlpatterns = [
    path('', views.denoise_image, name='denoise_image'),
    path('image/list/', views.image_list, name='image_list'),
    path('detail/<int:pk>/', views.image_detail, name='image_detail'),
    path('upload/', views.image_upload, name='image_upload'),
    path('update/<int:pk>/', views.image_update, name='image_update'),
    path('delete/<int:pk>/', views.image_delete, name='image_delete'),
]