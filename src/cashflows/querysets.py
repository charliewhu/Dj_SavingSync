from django.db import models
from django.utils.functional import cached_property

from django.db.models import Sum


class CashflowQuerySet(models.QuerySet):
    @cached_property
    def incomes(self):
        return self.filter(type="income")

    @cached_property
    def expenses(self):
        return self.filter(type="expense")

    @cached_property
    def monthly_balance(self):
        incomes = self.incomes.aggregate(amount=Sum("amount")).get("amount") or 0
        expenses = self.expenses.aggregate(amount=Sum("amount")).get("amount") or 0

        return incomes - expenses

    @cached_property
    def biannual_balance(self):
        return self.monthly_balance * 6

    @cached_property
    def annual_balance(self):
        return self.monthly_balance * 12
