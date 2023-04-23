from django.shortcuts import render, redirect
from store.forms import StoreForm
from store.models import Store

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


def show(request):
    stores = Store.objects.all()
    return render(request, "store/show.html", {'stores': stores})


def edit(request, id):
    store = Store.objects.get(id=id)
    return render(request, 'store/edit.html', {'store': store})


def update(request, id):
    store = Store.objects.get(id=id)
    form = StoreForm(request.POST, instance=store)
    if form.is_valid():
        form.save()
        return redirect("/stores/index")
    return render(request, 'store/edit.html', {'store': store})


def destroy(request, id):
    store = Store.objects.get(id=id)
    store.delete()
    return redirect("/stores/index")
