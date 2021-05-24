from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)
def new_show(request):
    return render(request, 'create.html')
def back(request):
    return redirect("/")
def create(request):
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description'],
    )
    return redirect('/')