from django.db import models
from django.db.models import Sum


class CashflowQuerySet(models.QuerySet):
    def monthly_balance(self):
        return self.aggregate(amount=Sum("amount")).get("amount")

    def biannual_balance(self):
        return self.aggregate(amount=Sum("amount")).get("amount") * 6
