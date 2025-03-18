from django.urls import path
from .views import FileUploaderView

urlpatterns = [
    path("" , FileUploaderView, name="upload_file_name")
]