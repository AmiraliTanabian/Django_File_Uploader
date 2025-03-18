from django import forms
from .models import  FileUploaderModel

class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = FileUploaderModel
        fields = "__all__"

        labels = {
            "file" :  ""
        }

        error_messages = {
            "file" : {"required":"لطفا فایل مورد نظر را انتخاب کنید!"}
        }

        widgets = {
            "file" : forms.FileInput(attrs = {"id":"file-upload", "class":"hidden"} )
        }