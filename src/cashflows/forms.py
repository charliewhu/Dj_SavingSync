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
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input input-bordered input-accent w-full max-w-xs"}
            ),
        }
