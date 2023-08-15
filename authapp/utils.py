from dateutil.relativedelta import relativedelta
from core.models import FinancialStatus


class CalculateAutoFields:
    def __init__(self, instance):
        self.instance = instance
        self.call()

    def calc_totalPrice(self):
        instance = self.instance

        # Remove starting fee 
        amountWithoutFee = instance.costProduct - instance.startingFee 

        # calculate total price without startingfee
        self.totalPrice = (instance.taxRate / 100) * amountWithoutFee + amountWithoutFee


    def calc_duration(self):
        instance = self.instance

        # calculate duration in months
        duration = relativedelta(instance.finishedAt, instance.startedAt)
        
        # Convert to normal nums
        self.duration = duration.months + 12 * duration.years
        self.duration += 1
    

    def calc_monthlyPayment(self):
        # Calculate monthly payment of customer
        self.amountOfMonth = self.totalPrice / self.duration


    

    def call(self):
        self.calc_totalPrice()
        self.calc_duration()
        self.calc_monthlyPayment()