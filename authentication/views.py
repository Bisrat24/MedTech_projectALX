from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from store.forms import StoreForm
from store.models import Store

from .forms import ProfileForm
from .models import Profile


def register(request):
    form = UserCreationForm()
    tform = ProfileForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user_id=user.id, type=request.POST.get('type'))
            if request.POST.get('type') == 'pharmacy':
                return redirect('pharmacy_register', user.id)
            return redirect('login')
    form.fields['username'].widget.attrs['class'] = 'form-control'
    form.fields['password1'].widget.attrs['class'] = 'form-control'
    form.fields['password2'].widget.attrs['class'] = 'form-control'
    tform.fields['type'].widget.attrs['class'] = 'form-control'
    return render(request, 'auth/register.html', {'form': form, 'tform': tform, 'title': 'Register'})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and validate_user(user):
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/login.html', {'error': 'Invalid credentials or Profile not approved', 'title': 'Login'})
    return render(request, 'auth/login.html', {'title': 'Login'})


def logout_user(request):
    logout(request)
    return redirect('login')


def validate_user(user):
    store = Store.objects.filter(owner=user).first()
    if user.profile.type == 'pharmacy':
        if store and store.is_approved:
            return True
        return False
    return True


def pharmacy_register(request, user):
    form = StoreForm()
    if request.method == 'POST':
        form = StoreForm(request.POST)
        usr = User.objects.get(id=user)
        if form.is_valid() and usr is not None and usr.profile.type == 'pharmacy':
            Store.objects.create(
                owner=usr, name=request.POST.get('name'), location=request.POST.get('location'), phone=request.POST.get('phone'))
            return redirect('login')
    form.fields['name'].widget.attrs['class'] = 'form-control'
    form.fields['location'].widget.attrs['class'] = 'form-control'
    form.fields['phone'].widget.attrs['class'] = 'form-control'
    return render(request, 'auth/pharmacy_register.html', {'form': form, 'title': 'Register Pharmacy'})
