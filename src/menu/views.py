from django.shortcuts import render, redirect, get_object_or_404

from menu.forms import MenuForm
from menu.models import MenuModel


# Create your views here.
def home(request):
    return render(request, 'base.html')




def list_menu(request):
    menus = MenuModel.objects.filter(status=True)
    total = menus.count()
    context = {
        'menus': menus,
        'total': total,
    }
    search_field=request.GET.get('search_field')
    if search_field:
        menus = MenuModel.objects.filter(plat__name__icontains=search_field)
        total = menus.count()
        context['menus']  =menus
        context['search_field'] = search_field

   
    return render(request, 'menus.html', context)


def add_menu(request):
    if request.method == 'POST':
        menu_form = MenuForm(request.POST)
        if menu_form.is_valid():
            menu_form.save()
            return redirect('menu:list')
    menu_form = MenuForm()
    context = {
        'form': menu_form,
    }
    return render(request, 'forms.html', context)


def edit_menu(request,id):
    menu = get_object_or_404(MenuModel,id=id)
    if request.method == 'POST':
        menu_form = MenuForm(request.POST,instance=menu)
        if menu_form.is_valid():
            menu_form.save()
            return redirect('menu:list')
    menu_form = MenuForm(instance=menu)
    context = {
        'form': menu_form,
    }
    return render(request, 'forms.html', context)


def delete_menu(request,id):
    menu = get_object_or_404(MenuModel,id=id)
    menu.status = False
    menu.save()
    return redirect('menu:list')

