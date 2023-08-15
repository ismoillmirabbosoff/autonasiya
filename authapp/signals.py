from django.db.models.signals import post_save
from authapp.models import ProductPurchase
from django.dispatch import receiver
from core.models import FinancialStatus
from .utils import CalculateAutoFields


@receiver(post_save, sender=ProductPurchase)
def auto_calculate(sender, instance, created, **kwargs):

    if created:
        FinancialStatus.objects.create(productPurchase=instance, amount=0.0)
        autoFields = CalculateAutoFields(instance=instance)
        instance.duration = autoFields.duration
        instance.nextPaymentAmount = autoFields.amountOfMonth


    autoFields = CalculateAutoFields(instance=instance)
    instance.totalPrice = autoFields.totalPrice
    instance.amountOfMonth = autoFields.amountOfMonth

    post_save.disconnect(auto_calculate, sender=ProductPurchase)

    instance.save()

    post_save.connect(auto_calculate, sender=ProductPurchase)
