from django.db import models

class FileUploaderModel(models.Model):
    file = models.FileField(upload_to="Files/", null=True)
    
