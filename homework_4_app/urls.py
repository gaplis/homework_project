from django.urls import path
from .views import update_product, upload_image_product


urlpatterns = [
    path('update_product/', update_product, name='update_product'),
    path('upload_image_product/', upload_image_product, name='upload_image_product'),
]