from django.db import models
from django.db.models import Sum


class CashflowQuerySet(models.QuerySet):
    def incomes(self):
        return self.filter(type="income")

    def expenses(self):
        return self.filter(type="expense")

    def monthly_balance(self):
        return self.aggregate(amount=Sum("amount")).get("amount", 0)

    def biannual_balance(self):
        return self.aggregate(amount=Sum("amount")).get("amount", 0) * 6

    def annual_balance(self):
        return self.aggregate(amount=Sum("amount")).get("amount", 0) * 12
