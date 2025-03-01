from django import forms
from .models import Newspaper

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = ['title', 'publisher', 'publication_date', 'language', 'cover_image']