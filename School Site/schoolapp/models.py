from django.db import models

# Create your models here.

class principal_login(models.Model):
    role=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
