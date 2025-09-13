from django.urls import path
from . import views

app_name = "expenditure"

urlpatterns = [
    path("", views.expenditure_list, name="expenditure_list"),
    path("add/", views.expenditure_add, name="expenditure_add"),
    path("<int:pk>/edit/", views.expenditure_edit, name="expenditure_edit"),
    path("<int:pk>/delete/", views.expenditure_delete, name="expenditure_delete"),
]
