from django import forms
from .models import CounterW


class CounterWForm(forms.ModelForm):
    class Meta:
        model = CounterW
        fields = (
            'month',
            'year',
            'comment',
            'indication',
            'home',)
