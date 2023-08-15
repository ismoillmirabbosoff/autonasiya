from django.contrib import admin
from .models import FinancialStatus


@admin.register(FinancialStatus)
class FinanceAdmin(admin.ModelAdmin):
    list_display = ("productPurchase", "amount")

