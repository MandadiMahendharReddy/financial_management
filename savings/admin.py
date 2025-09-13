from django.contrib import admin
from .models import Saving

@admin.register(Saving)
class SavingAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'target', 'description')
    search_fields = ('target', 'description')
    list_filter = ('date', 'target')
