from django.db import models
import shortuuid
from django.utils import timezone



class Customer(models.Model):
    checkId = models.CharField("Check Id", max_length=25, default=shortuuid.uuid)
    firstName = models.CharField("Ism", max_length=255)
    phoneNumber = models.CharField("Tel.raqam", max_length=255, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phoneNumber}"


    class Meta:
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"

STATUS_CHOISES = (
    ("OPEN", "Ochiq"),
    ("CLOSE", "Yopiq"),
)

class ProductPurchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="purchases")
    productName = models.CharField("Maxsulot nomi", max_length=255)
    costProduct = models.FloatField("Maxsulot tan narxi")
    startingFee = models.FloatField("Boshlang'ich to'lov", default=0.0)
    taxRate = models.FloatField("Soliq foizi")
    amountOfMonth = models.FloatField("Oylik tolov", null=True, blank=True)
    totalPrice = models.FloatField("Ummumiy summa", null=True, blank=True)

    nextPaymentAmount = models.FloatField("Keyingi to'lov summasi", null=True, blank=True)
    duration = models.FloatField("Davomiyligi", null=True, blank=True)
    status = models.CharField("Xisob", choices=STATUS_CHOISES, max_length=5, default="OPEN")
    startedAt = models.DateTimeField("Boshlanish sanasi", default=timezone.now)
    finishedAt = models.DateTimeField("Tugash sanasi")


    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"

    def __str__(self):
        return f"{self.customer.phoneNumber}, {self.productName}"
