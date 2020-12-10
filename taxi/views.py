from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image
from django import forms
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks     
from .forms import PhotoForm

# Create your views here.
def index(request):
    return render(request, 'Page/index.html')

def taxi(request):
    images = Image.objects.all()
    
    return render(request, 'taxi/taxi.html', {'images': images[::-1]})