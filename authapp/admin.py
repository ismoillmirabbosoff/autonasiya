from django.contrib import admin
from .models import Customer, ProductPurchase
from core.models import Payment


class ProductPurchaseInline(admin.TabularInline):
    model = ProductPurchase
    readonly_fields = ("id", "totalPrice", "amountOfMonth", "duration", "nextPaymentAmount", "status")
    extra = 1


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False


    def has_change_permission(self, request, obj=None):
        return False



@admin.register(ProductPurchase)
class ProductPurchaseAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]

    def get_customer_checkid(self, obj):
        return obj.customer.checkId
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # obj is None when creating a new instance
            return self.readonly_fields + ('startedAt', "finishedAt", "costProduct", "startingFee", "taxRate")
        return self.readonly_fields


    get_customer_checkid.short_description = "Customer Check ID"

    readonly_fields = ("id", "totalPrice", "amountOfMonth", "duration",  "nextPaymentAmount", "status")
    list_display = ("customer",  "productName", "get_customer_checkid", "nextPaymentAmount", "totalPrice", "duration", "status")
    search_fields = ("productName", "customer__checkId", "status")
    list_filter = ("customer", "status")


    




@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [ProductPurchaseInline]
    list_display = ("firstName", "phoneNumber", "checkId")
    search_fields = ("phoneNumber", "checkId", "firstName")