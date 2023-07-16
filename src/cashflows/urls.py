from django.urls import path
from .views import home, create_cashflow_view, delete_cashflow_view

urlpatterns = [
    path("", home, name="home"),
    path("create", create_cashflow_view, name="create_cashflow"),
    path("<int:id>/delete", delete_cashflow_view, name="delete_cashflow"),
]
