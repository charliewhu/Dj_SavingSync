from django.http import HttpRequest, HttpResponse
from django.db.models import Sum
from django.shortcuts import redirect, render
from django.urls import reverse


from .forms import CashflowForm
from .models import Cashflow


# Create your views here.
def home(request: HttpRequest):
    form = CashflowForm()
    cashflows = Cashflow.objects.all()
    incomes = cashflows.filter(type="INCOME")
    expenses = cashflows.filter(type="EXPENSE")
    monthly_balance = cashflows.aggregate(amount=Sum("amount"))

    context = {
        "form": form,
        "incomes": incomes,
        "expenses": expenses,
        "monthly_balance": monthly_balance["amount"],
    }

    return render(
        request,
        "home.html",
        context,
    )


def create_cashflow_view(request: HttpRequest):
    form = CashflowForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect(reverse("home"))


def delete_cashflow_view(request: HttpRequest):
    return redirect(reverse("home"))
