from django.contrib import admin

# Register your models here.
from .models import Show

class ShowAdmin(admin.ModelAdmin):
    model= Show

admin.site.register(Show, ShowAdmin)