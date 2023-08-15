from dateutil.relativedelta import relativedelta
from .models import FinancialStatus, Payment
import math

from django.db.models import Sum

class FinanceManager:
    def __init__(self, instance):
        self.instance = instance
        self.product = instance.productPurchase
        self.financialObj = FinancialStatus.objects.get(productPurchase=self.product)
        self.payedAmount = instance.amount
        self.defaultMonthlyAmount = self.product.amountOfMonth


    def addFinanceSum(self):
        """"
        This method adds extra or debt sum to finance obj. 
        If customer pays in default monthly payment it will be always 0
        """
        self.financialObj.amount = self.financialObj.amount + (self.payedAmount - self.defaultMonthlyAmount)
        self.financialObj.save()


    def isClosed(self):
        allPayedAmount = Payment.objects.filter(productPurchase=self.product).aggregate(Sum('amount'))['amount__sum'] or 0
        return allPayedAmount >= self.product.totalPrice


    def setNextPaymentAmount(self):
        rangeMonths = self.product.finishedAt.month - self.instance.date.month
        
        # If this previous month of last month
        #         
        if rangeMonths == 1:
            # section #check last month - https://docs.google.com/document/d/1RxFlEc4-mMgJ3_PT339mJFmpdP4DBo-cbwAamCE9sgk/edit
            reverseSum = self.financialObj.amount * -1
            self.product.nextPaymentAmount =  self.defaultMonthlyAmount + (reverseSum)
        
        elif self.isClosed():
            self.product.status = "CLOSE"
            self.product.nextPaymentAmount = 0
    
        else:
            self.product.nextPaymentAmount = self.defaultMonthlyAmount


        self.product.save()
        self.instance.save()

    def removeDuration(self):
        
        # There will get extraSum 
        # #Get extra sum section - https://docs.google.com/document/d/1RxFlEc4-mMgJ3_PT339mJFmpdP4DBo-cbwAamCE9sgk/edit
        months = self.months
        delta = self.delta

        extraSum = self.payedAmount - self.defaultMonthlyAmount * months 
        
        # Add this extra sum to financeSum.
        self.financialObj.amount = extraSum

        if self.type_ == "minus":
            self.product.duration -= months
            self.product.finishedAt = self.product.finishedAt - delta

        self.financialObj.save()


    def controlDuration(self, type_):
        """
            There will be checks payed sum and 
            if it is higher than default monthly payment will be minus duration and if we will have extra money we will add this to financeSum
            if it is lower than default. We will calculate this debt sum and add to financeSum
        """

        # get calculated duration from financeSum

        self.durationFloatMonth = float(self.financialObj.amount / self.defaultMonthlyAmount)

        # If duration will be higher than 1.0 it means customer payed higher than default

        self.months = math.floor(self.durationFloatMonth)  # The months part
        self.delta = relativedelta(months=self.months)

        if self.durationFloatMonth > 1.0:
            # Always do round lower and minus from duration and finishedAt
            self.type_ = type_
            self.removeDuration()
            
        self.financialObj.save()
        self.product.save()


    def adding(self):
        self.addFinanceSum()
        # Remove duration
        self.controlDuration(type_="minus")
        self.setNextPaymentAmount()

