from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CashflowForm
from .models import Cashflow


# Create your views here.
def home(request: HttpRequest):
    form = CashflowForm()
    cashflows = Cashflow.objects.all().order_by("-amount")
    cashflow_percentages = cashflows.expense_percentages()  # type: ignore

    context = {
        "form": form,
        "cashflows": cashflows,
        "cashflow_percentages": cashflow_percentages,
    }

    return render(
        request,
        "cashflows/home.html",
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
