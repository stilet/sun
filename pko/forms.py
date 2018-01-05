from django import forms
from .models import Pko


class PkoForm(forms.ModelForm):
    class Meta:
        model = Pko
        fields = (
            'month',
            'year',
            'comment',
            'summ_e',
            'summ_w',
            'summ_fond',
            'home',)
