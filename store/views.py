from django.shortcuts import render, redirect
from store.forms import StoreForm
from store.models import Store
from drugs.models import Drugs
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def create_store(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/stores/index')
            except:
                pass
    else:
        form = StoreForm()
    return render(request, 'store/index.html', {'form': form})


@login_required(login_url="/login/")
def show(request):
    stores = Store.objects.all()
    return render(request, "store/show.html", {'stores': stores})


@login_required(login_url="/login/")
def single(request, id):
    store = Store.objects.get(id=id)
    drugs = Drugs.objects.filter(pharmacy=store)
    return render(request, "store/single.html", {'store': store, 'drugs': drugs})


@login_required(login_url="/login/")
def edit(request, id):
    store = Store.objects.get(id=id)
    return render(request, 'store/edit.html', {'store': store})


@login_required(login_url="/login/")
def update(request, id):
    store = Store.objects.get(id=id)
    form = StoreForm(request.POST, instance=store)
    if form.is_valid():
        form.save()
        return redirect("/stores/index")
    return render(request, 'store/edit.html', {'store': store})


@login_required(login_url="/login/")
def destroy(request, id):
    store = Store.objects.get(id=id)
    store.delete()
    return redirect("/stores/index")
