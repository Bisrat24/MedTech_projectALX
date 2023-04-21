from django.shortcuts import render, redirect
from drugs.forms import DrugsForm
from drugs.models import Drugs

def create_drug(request):
    if request.method == "POST":
        form = DrugsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/drugs/index')
            except:
                pass
    else:
        form = DrugsForm()
    return render(request, 'drugs/index.html', {'form': form})


def show(request):
    drugs = Drugs.objects.all()
    return render(request, "drugs/show.html", {'drugs': drugs})


def edit(request, id):
    drug = Drugs.objects.get(id=id)
    return render(request, 'drugs/edit.html', {'drug': drug})


def update(request, id):
    drug = Drugs.objects.get(id=id)
    form = DrugsForm(request.POST, instance=drug)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'drugs/edit.html', {'drug': drug})


def destroy(request, id):
    drug = Drugs.objects.get(id=id)
    drug.delete()
    return redirect("/drugs/index")
