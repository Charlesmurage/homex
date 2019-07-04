from .models import Business
from django import forms

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['resident',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }