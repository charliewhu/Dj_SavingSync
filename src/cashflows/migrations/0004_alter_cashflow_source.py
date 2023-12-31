# Generated by Django 4.2.3 on 2023-07-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cashflows", "0003_alter_cashflow_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cashflow",
            name="source",
            field=models.CharField(
                choices=[
                    ("salary", "Salary"),
                    ("regular_bill", "Regular Bill"),
                    ("savings", "Savings"),
                ],
                max_length=20,
            ),
        ),
    ]
