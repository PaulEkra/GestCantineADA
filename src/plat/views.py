from django.shortcuts import render, redirect, get_object_or_404

from plat.models import PlatModel
from plat.forms import PlatForm


# Create your views here.
def list_plat(request):
    plats = PlatModel.objects.filter(status=True)
    total = plats.count()
    context = {
        'plats': plats,
        'total': total,
    }
    search_field=request.GET.get('search_field')
    if search_field:
        plats = PlatModel.objects.filter(name__icontains=search_field)
        total = plats.count()
        context['plats']  =plats
        context['search_field'] = search_field

   
    return render(request, 'plats.html', context)


def add_plat(request):
    if request.method == 'POST':
        plat_form = PlatForm(request.POST)
        if plat_form.is_valid():
            plat_form.save()
            return redirect('plat:list')
    plat_form = PlatForm()
    context = {
        'form': plat_form,
    }
    return render(request, 'forms.html', context)


def edit_plat(request,id):
    plat = get_object_or_404(PlatModel,id=id)
    if request.method == 'POST':
        plat_form = PlatForm(request.POST,instance=plat)
        if plat_form.is_valid():
            plat_form.save()
            return redirect('plat:list')
    plat_form = PlatForm(instance=plat)
    context = {
        'form': plat_form,
    }
    return render(request, 'forms.html', context)


def delete_plat(request,id):
    plat = get_object_or_404(PlatModel,id=id)
    plat.status = False
    plat.save()
    return redirect('plat:list')
