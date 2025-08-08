from django import forms
from .models import Booking


class EditingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start', 'end']
        widgets = {
            'start': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'step': 1800
            }),
            'end': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'step': 1800
            }),
        }