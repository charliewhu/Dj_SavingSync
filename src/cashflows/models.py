from django.db import models


# Create your models here.
class Cashflow(models.Model):
    TYPE_CHOICES = [
        ("INCOME", "Income"),
        ("EXPENSE", "Expense"),
    ]

    SOURCE_CHOICES = [
        ("SALARY", "Salary"),
        ("REGULAR_BILL", "Regular Bill"),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
