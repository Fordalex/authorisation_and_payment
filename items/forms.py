from django import forms
from django.forms import ModelForm
from .models import Item

class inputItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'category', 'time', 'author')