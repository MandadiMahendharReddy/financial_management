from django.shortcuts import render, redirect
from .models import Income
from .forms import IncomeForm
from django.db import models
import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user).order_by("-date")
    total_income = incomes.aggregate(total=models.Sum("amount"))["total"] or 0
    return render(request, "income/income_list.html", {"incomes": incomes, "total_income": total_income})


def income_add(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user  # 👈 Assign the logged-in user
            form.save()
            return redirect("income:income_list")
    else:
        form = IncomeForm()
    return render(request, "income/income_form.html", {"form": form})

def income_edit(request, pk):
    income = Income.objects.get(pk=pk)
    if request.method == "POST":
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user  # 👈 Assign the logged-in user
            form.save()
            return redirect("income:income_list")
    else:
        form = IncomeForm(instance=income)
    return render(request, "income/income_form.html", {"form": form})

def income_delete(request, pk):
    income = Income.objects.get(pk=pk)
    if request.method == "POST":
        income.delete()
        return redirect("income:income_list")
    return render(request, "income/income_confirm_delete.html", {"income": income})
