# Generated by Django 4.2.3 on 2023-07-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cashflows", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cashflow",
            name="source",
            field=models.CharField(
                choices=[("salary", "Salary"), ("regular_bill", "Regular Bill")],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="cashflow",
            name="type",
            field=models.CharField(
                choices=[("income", "Income"), ("expense", "Expense")], max_length=10
            ),
        ),
    ]
