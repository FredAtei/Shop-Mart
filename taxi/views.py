from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import Image,Profile
from django import forms
from django.http import HttpResponse
from cloudinary.forms import cl_init_js_callbacks     
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from .forms import UpdateUserForm,UpdateUserProfileForm

# Create your views here.
def index(request):
    return render(request, 'Page/index.html')

@login_required(login_url='/accounts/login/')
def taxi(request):
    images = Image.objects.all()
    
    return render(request, 'taxi/taxi.html', {'images': images[::-1]})

def profile(request,profile_id):
    profile = Profile.objects.filter(id=profile_id)
    # images = request.user.profile.images.all()
    current_user = request.user
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST )
        profile_form = UpdateUserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            profile_form.save()
            bio = user.bio
    else:
        user_form = UpdateUserForm()
        prof_form = UpdateUserProfileForm()
    params = {
        'user_form': user_form,
        'profile_form': prof_form, 
        'profile':profile  

    }
    return render(request, 'profile.html', params)    