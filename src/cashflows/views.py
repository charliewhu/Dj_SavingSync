from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from src.cashflows.forms import CashflowForm


# Create your views here.
def home(request: HttpRequest):
    form = CashflowForm()
    context = {
        "form": form,
    }

    return render(
        request,
        "home.html",
        context,
    )


def create(request: HttpRequest):
    return redirect(reverse("home"))
