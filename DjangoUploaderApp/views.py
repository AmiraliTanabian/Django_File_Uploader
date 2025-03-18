from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import FileUploadModelForm

class FileUploaderView(CreateView):
    form_class = FileUploadModelForm
    success_url = reverse_lazy("upload_file_name")
    template_name = "index.html"
    context_object_name = "form"