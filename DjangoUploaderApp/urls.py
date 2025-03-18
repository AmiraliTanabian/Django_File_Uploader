from django.urls import path
from .views import FileUploaderView

urlpatterns = [
    path("" , FileUploaderView.as_view() , name="upload_file_name")
]