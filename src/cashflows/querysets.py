from django.db import models
from django.db.models import Sum


class CashflowQuerySet(models.QuerySet):
    def incomes(self):
        return self.filter(type="income")

    def expenses(self):
        return self.filter(type="expense")

    def monthly_balance(self):
        incomes = (
            self.filter(type="income").aggregate(amount=Sum("amount")).get("amount")
        ) or 0
        expenses = (
            self.filter(type="expense").aggregate(amount=Sum("amount")).get("amount")
        ) or 0

        return incomes - expenses

    def biannual_balance(self):
        return self.monthly_balance() * 6

    def annual_balance(self):
        return self.monthly_balance() * 12
