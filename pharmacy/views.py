from django.shortcuts import render, redirect
from store.forms import StoreForm
from store.models import Store


def home(request):
    return render(request, "home.html")
