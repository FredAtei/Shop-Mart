from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image
from django import forms
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks     
from .forms import PhotoForm

# Create your views here.
def index(request):
    pictures = Picture.objects.all()
    ctx = {'pictures': pictures}
    return render(request, 'Page/index.html', ctx)

def upload(request):
  context = dict( backend_form = PhotoForm())

  if request.method == 'POST':
    form = PhotoForm(request.POST, request.FILES)
    context['posted'] = form.instance
    if form.is_valid():
        form.save()

  return render(request, 'upload.html', context)
  
def photos(request):
    images = Image.get_images()
    return render(request, 'all-photos/all_photos.html',{"images":images})