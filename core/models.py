from django.db import models
from authapp.models import ProductPurchase
from django.utils import timezone



class Payment(models.Model):
    productPurchase = models.ForeignKey(ProductPurchase, on_delete=models.CASCADE, related_name="payments")
    date = models.DateField("To'lov Sanasi", default=timezone.now)
    amount = models.FloatField("Summa")
    createdAt = models.DateTimeField(auto_now_add=True)
    


class FinancialStatus(models.Model):
    productPurchase = models.ForeignKey(ProductPurchase, on_delete=models.CASCADE, related_name="financies")
    amount = models.FloatField("Summa")

    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Finance"
        verbose_name_plural = "Finances"


    def __str__(self):
        return f"{self.productPurchase}, {self.amount}"

