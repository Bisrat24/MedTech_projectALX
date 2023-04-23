from django.shortcuts import render, redirect
from store.forms import StoreForm
from store.models import Store
from drugs.models import Drugs


def home(request):
    if request.user.is_authenticated:
        drugs = Drugs.objects.all()
        stores = Store.objects.all()
        return render(request, "home.html", {"drugs": drugs, "stores": stores})
    return render(request, "home.html")
