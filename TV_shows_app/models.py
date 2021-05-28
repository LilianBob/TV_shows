from django.db import models
from django.db.models.fields import CharField
from django.forms import ModelForm

# Create your models here.
class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.CharField(max_length=255)
    release_date= models.DateField(blank=True, null=True)
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
class ReleaseDate(ModelForm):
    class Meta:
        model = Show
        fields = ['release_date']