from django import forms

from plat.models import PlatModel
from .models import MenuModel


class MenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        plat_ids = MenuModel.objects.values_list('plat_id', flat=True)
        self.fields['plat'].queryset = PlatModel.objects.exclude(id__in=plat_ids)

    class Meta:
        model = MenuModel
        fields = ['plat']
