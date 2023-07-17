from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CashflowForm
from .models import Cashflow


# Create your views here.
def home(request: HttpRequest):
    form = CashflowForm()
    cashflows = Cashflow.objects.all()
    incomes = cashflows.filter(type="income")
    expenses = cashflows.filter(type="expense")

    monthly_balance = cashflows.monthly_balance()
    biannual_balance = cashflows.biannual_balance()

    context = {
        "form": form,
        "incomes": incomes,
        "expenses": expenses,
        "monthly_balance": monthly_balance,
        "biannual_balance": biannual_balance,
    }

    return render(
        request,
        "home.html",
        context,
    )


def create_cashflow_view(request: HttpRequest):
    form = CashflowForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return redirect(reverse("home"))


def delete_cashflow_view(request: HttpRequest, id):
    if request.method == "POST":
        Cashflow.objects.get(id=id).delete()
    return redirect(reverse("home"))
