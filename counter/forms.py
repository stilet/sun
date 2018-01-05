from django import forms
from .models import CounterE


# Модель счетчика электричества индивидуального.
class CounterEForm(forms.ModelForm):
    class Meta:
        model = CounterE
        fields = (
            'month',
            'year',
            'comment',
            'indication_day',
            'indication_night',
            'home',)
