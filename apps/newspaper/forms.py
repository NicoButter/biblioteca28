from django import forms
from .models import Newspaper

class NewspaperForm(forms.ModelForm):
    class Meta:
        model = Newspaper
        fields = [
            'title', 
            'copete',
            'publisher', 
            'publication_date', 
            'language',
            'scope',  
            'genre', 
            'edition', 
            'description', 
            'cover_image', 
            'status', 
            'physical_location', 
            'issn', 
            'pages', 
            'price'
        ]