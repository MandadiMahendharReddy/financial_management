from django.contrib import admin
from .models import Income

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'source', 'description')
    search_fields = ('source', 'description')
    list_filter = ('date', 'source')
