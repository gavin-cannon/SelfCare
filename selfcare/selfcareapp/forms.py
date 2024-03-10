# forms.py

from django import forms
from .models import SelfCareItem

class SelfCareItemForm(forms.ModelForm):
    class Meta:
        model = SelfCareItem
        fields = ['title', 'description', 'completed']