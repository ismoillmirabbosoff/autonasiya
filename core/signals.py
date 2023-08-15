from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Payment
from .utils import FinanceManager

@receiver(post_save, sender=Payment)
def add_financeSum(sender, instance, created, **kwargs):

    if created:
        FinanceManager(instance).adding()


# @receiver(pre_delete, sender=Payment)
# def remove_financeSum(sender, instance, **kwargs):
#     FinanceManager(instance).remove()







        