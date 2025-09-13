from django.contrib import admin
from .models import Expenditure

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'category', 'description')
    search_fields = ('category', 'description')
    list_filter = ('date', 'category')
