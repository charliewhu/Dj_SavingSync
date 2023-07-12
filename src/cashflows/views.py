from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.
def home(request: HttpRequest):
    return render(request, "home.html")


def create(request: HttpRequest):
    return redirect(reverse("home"))
