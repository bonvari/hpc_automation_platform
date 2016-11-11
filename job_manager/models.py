from django.db import models


# Create your models here.

class Job(models.Model):
    file_first = models.FileField(upload_to='uploads/%Y_%m_%d/')
    file_second = models.FileField(upload_to='uploads/%Y_%m_%d/')
    file_third = models.FileField(upload_to='uploads/%Y_%m_%d/', blank=True)
    file_forth = models.FileField(upload_to='uploads/%Y_%m_%d/', blank=True)
    email = models.EmailField()
    hostname = models.CharField(max_length=100, default='aoclsb.uab.cat')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)
    result = models.TextField(blank=True)
    state = models.BooleanField(default=False)
    latest_run = models.IntegerField(default=1)
