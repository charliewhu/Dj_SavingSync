from django.db import models
from django.utils.functional import cached_property

from django.db.models import Sum, Q


class CashflowQuerySet(models.QuerySet):
    @cached_property
    def incomes(self):
        return self.filter(type="income")

    @cached_property
    def expenses(self):
        return self.filter(Q(type="need") | Q(type="want") | Q(type="saving"))

    @cached_property
    def monthly_income(self):
        return self.incomes.aggregate(amount=Sum("amount")).get("amount") or 0

    @cached_property
    def monthly_expenses(self):
        return self.expenses.aggregate(amount=Sum("amount")).get("amount") or 0

    @cached_property
    def monthly_balance(self):
        return self.monthly_income - self.monthly_expenses

    @cached_property
    def biannual_balance(self):
        return self.monthly_balance * 6

    @cached_property
    def annual_balance(self):
        return self.monthly_balance * 12

    def expense_percentages(self):
        x = self.aggregate(
            needs=Sum("amount", filter=Q(type="need")) * 100 / self.monthly_income,
            wants=Sum("amount", filter=Q(type="want")) * 100 / self.monthly_income,
            savings=Sum("amount", filter=Q(type="saving")) * 100 / self.monthly_income,
        )

        return x
