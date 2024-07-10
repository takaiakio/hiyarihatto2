from django import forms
from .models import HiyariHatto

class HiyariHattoForm(forms.ModelForm):
    class Meta:
        model = HiyariHatto
        fields = ['title', 'process', 'action', 'situation', 'consequence', 'avoidance', 'danger_level', 'phase']

