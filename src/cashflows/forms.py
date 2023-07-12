from django.forms import ModelForm
from .models import Cashflow


class CashflowForm(ModelForm):
    class Meta:
        model = Cashflow
        fields = [
            "type",
            "source",
            "name",
            "amount",
        ]
