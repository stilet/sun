from django import forms
from .models import Rko


class RkoForm(forms.ModelForm):
    class Meta:
        model = Rko
        fields = (
            'month',
            'year',
            'comment',
            'summ_fond',)
