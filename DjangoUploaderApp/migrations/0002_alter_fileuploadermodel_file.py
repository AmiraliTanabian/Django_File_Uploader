# Generated by Django 5.1.7 on 2025-03-18 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoUploaderApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileuploadermodel',
            name='file',
            field=models.FileField(null=True, upload_to='Files/'),
        ),
    ]
