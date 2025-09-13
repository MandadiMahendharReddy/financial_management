from django import forms
from .models import Income
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Restore IncomeForm (for existing app functionality)
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'date', 'source', 'description']

# Registration form for custom user sign-up
class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, label="Full Name")
    email = forms.EmailField(required=True)
    dob = forms.DateField(required=True, label="Date of Birth", widget=forms.DateInput(attrs={"type": "date"}))
    phone = forms.CharField(max_length=20, required=True, label="Phone Number")

    class Meta:
        model = User
        fields = (
            "username",
            "full_name",
            "email",
            "dob",
            "phone",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with that email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        name = self.cleaned_data.get("full_name", "").strip()
        if " " in name:
            user.first_name, user.last_name = name.split(" ", 1)
        else:
            user.first_name = name
            user.last_name = ""
        user.email = self.cleaned_data.get("email")
        if commit:
            user.save()
        # Optionally, store dob/phone in profile or future extension
        return user
