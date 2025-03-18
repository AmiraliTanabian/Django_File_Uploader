from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import FileUploadModelForm
from django.contrib import messages

class FileUploaderView(CreateView):
    form_class = FileUploadModelForm
    success_url = reverse_lazy("upload_file_name")
    template_name = "index.html"
    context_object_name = "form"


    def form_valid(self, form):
        messages.success(self.request, "فرم با موفقیت ارسال شد")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.ERROR(self.request, "خطا در ارسال فایل!")
        return super().form_invalid(form)