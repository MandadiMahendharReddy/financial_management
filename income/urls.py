from django.urls import path
from . import views

app_name = "income"

urlpatterns = [
    path("", views.income_list, name="income_list"),
    path("add/", views.income_add, name="income_add"),
    path("<int:pk>/edit/", views.income_edit, name="income_edit"),
    path("<int:pk>/delete/", views.income_delete, name="income_delete"),
]
