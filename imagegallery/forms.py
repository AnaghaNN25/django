from django import forms
from .models import Imagegallery
class ImageForm(forms.ModelForm):
    class Meta:
        model=Imagegallery
        fields=('caption','image')