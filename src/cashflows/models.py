from django.db import models
from django.core.validators import MinValueValidator

from .querysets import CashflowQuerySet


# Create your models here.
class Cashflow(models.Model):
    TYPE_CHOICES = [
        ("income", "Income"),
        ("need", "Need"),
        ("want", "Want"),
        ("saving", "Saving"),
    ]

    SOURCE_CHOICES = [
        ("salary", "Salary"),
        ("regular_bill", "Regular Bill"),
        ("savings", "Savings"),
    ]

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
    )
    source = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES,
    )
    name = models.CharField(
        max_length=30,
    )
    amount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )

    objects = CashflowQuerySet.as_manager()
