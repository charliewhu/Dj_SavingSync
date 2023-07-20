from django import forms
from .models import Cashflow


class CashflowForm(forms.ModelForm):
    class Meta:
        model = Cashflow
        fields = [
            "type",
            "source",
            "name",
            "amount",
        ]
