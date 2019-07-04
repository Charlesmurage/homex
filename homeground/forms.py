from .models import Business

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['resident',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }