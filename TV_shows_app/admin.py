from django.contrib import admin

# Register your models here.
from .models import Show
from .forms import ShowRelease

class ShowAdmin(admin.ModelAdmin):
    model= Show
    form= ShowRelease

admin.site.register(Show, ShowAdmin)