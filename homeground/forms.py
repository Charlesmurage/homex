from .models import Business, Community
from django import forms

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['resident',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class NewCommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        exclude = ['resident',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }