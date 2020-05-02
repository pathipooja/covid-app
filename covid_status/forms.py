from .models import Country
from django.forms import ModelForm,TextInput


class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input' ,'placeholder':'State Name'})}