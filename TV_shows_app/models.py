from django.db import models

# Create your models here.
class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.CharField(max_length=255)
    release_date= models.DateField(auto_now_add=False, auto_now=False, null=True)
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
