from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .models import Profile
from store.models import *
from .forms import ProfileForm


def register(request):
    form = UserCreationForm()
    tform = ProfileForm()
    form.fields['username'].widget.attrs['class'] = 'form-control'
    form.fields['password1'].widget.attrs['class'] = 'form-control'
    form.fields['password2'].widget.attrs['class'] = 'form-control'
    tform.fields['type'].widget.attrs['class'] = 'form-control'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user_id=user.id, type=request.POST.get('type'))
            return redirect('login')
    return render(request, 'auth/register.html', {'form': form, 'tform': tform, 'title': 'Register'})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'auth/login.html', {'title': 'Login'})


def logout_user(request):
    logout(request)
    return redirect('login')
