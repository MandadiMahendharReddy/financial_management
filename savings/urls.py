from django.urls import path
from . import views

app_name = "savings"

urlpatterns = [
    path("", views.saving_list, name="saving_list"),
    path("add/", views.saving_add, name="saving_add"),
    path("<int:pk>/edit/", views.saving_edit, name="saving_edit"),
    path("<int:pk>/delete/", views.saving_delete, name="saving_delete"),
]
