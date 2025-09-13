from django.shortcuts import render, redirect
from .models import Expenditure
from .forms import ExpenditureForm
from django.db import models
import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def expenditure_list(request):
    expenditures = Expenditure.objects.filter(user=request.user).order_by("-date")
    total_expenditure = expenditures.aggregate(total=models.Sum("amount"))["total"] or 0
    return render(request, "expenditure/expenditure_list.html", {"expenditures": expenditures, "total_expenditure": total_expenditure})

def expenditure_add(request):
    if request.method == "POST":
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            expenditure=form.save(commit=False)
            expenditure.user = request.user  # 👈 Assign the logged-in user
            form.save()
            return redirect("expenditure:expenditure_list")
    else:
        form = ExpenditureForm()
    return render(request, "expenditure/expenditure_form.html", {"form": form})

def expenditure_edit(request, pk):
    expenditure = Expenditure.objects.get(pk=pk)
    if request.method == "POST":
        form = ExpenditureForm(request.POST, instance=expenditure)
        if form.is_valid():
            expenditure = form.save(commit=False)
            expenditure.user = request.user  # 👈 Assign the logged-in user
            form.save()
            return redirect("expenditure:expenditure_list")
    else:
        form = ExpenditureForm(instance=expenditure)
    return render(request, "expenditure/expenditure_form.html", {"form": form})

def expenditure_delete(request, pk):
    expenditure = Expenditure.objects.get(pk=pk)
    if request.method == "POST":
        expenditure.delete()
        return redirect("expenditure:expenditure_list")
    return render(request, "expenditure/expenditure_confirm_delete.html", {"expenditure": expenditure})
