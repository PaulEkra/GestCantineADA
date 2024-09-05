from django import forms

from .models import PlatModel


class PlatForm(forms.ModelForm):
    class Meta:
        model = PlatModel
        fields = ['name', 'summary']
        labels = {
            'name': '',
            'summary': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Nom du plat','class':"outline mb-3"}),
            'summary': forms.Textarea(attrs={'placeholder':'Summary','style':'border : 2px'}),
        }
        
        
