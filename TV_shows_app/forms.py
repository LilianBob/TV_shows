from django import forms
from .models import Show


class DateInput(forms.DateInput):
    input_type = 'date'


class ShowRelease(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['title', 'network', 'release_date', 'description']
        widgets = {
            'release_date': DateInput(),
        }