from django.shortcuts import render, redirect
from .models import Saving
from .forms import SavingForm
from django.db import models
import pandas as pd
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def saving_list(request):
    savings = Saving.objects.filter(user=request.user).order_by("-date")
    total_savings = savings.aggregate(total=models.Sum("amount"))["total"] or 0
    return render(request, "savings/saving_list.html", {"savings": savings, "total_savings": total_savings})

def saving_add(request):
    if request.method == "POST":
        form = SavingForm(request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.user = request.user  # 👈 Assign the logged-in user
            form.save()
            return redirect("savings:saving_list")
    else:
        form = SavingForm()
    return render(request, "savings/saving_form.html", {"form": form})

def saving_edit(request, pk):
    saving = Saving.objects.get(pk=pk)
    if request.method == "POST":
        form = SavingForm(request.POST, instance=saving)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.user = request.user  # 👈 Assign the logged-in user
            form.save()
            return redirect("savings:saving_list")
    else:
        form = SavingForm(instance=saving)
    return render(request, "savings/saving_form.html", {"form": form})

def saving_delete(request, pk):
    saving = Saving.objects.get(pk=pk)
    if request.method == "POST":
        saving.delete()
        return redirect("savings:saving_list")
    return render(request, "savings/saving_confirm_delete.html", {"saving": saving})
