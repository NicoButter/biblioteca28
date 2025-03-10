from django import forms
from .models import Cardex

class CardexForm(forms.ModelForm):
    class Meta:
        model = Cardex
        fields = ['circulation', 'issue_number', 'content_summary']
        widgets = {
            'content_summary': forms.Textarea(attrs={'rows': 4}),
        }
        