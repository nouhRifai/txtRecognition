# Generated by Django 3.1.7 on 2021-03-01 19:39

import apiapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awsimage',
            name='images',
        ),
        migrations.AddField(
            model_name='awsimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apiapp.models.upload_path),
        ),
    ]
