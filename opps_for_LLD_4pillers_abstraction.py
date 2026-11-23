#...............................................................
#---------------------------bad practice------------------------

class StripeAPI:
    def process_payment(self, amount):
        print(f"Processing Stripe payment: {amount}")


class OrderService:
    def __init__(self):
        self.payment = StripeAPI()

    def checkout(self, amount):
        self.payment.process_payment(amount)


service = OrderService()
service.checkout(5000)

#problem:
#OrderService directly depends on StripeAPI.
#if we want to use Razorpay or PayPal, we need to modify OrderService.
#__________________________________________________________________

#---------------------------good practice--------------------------
from abc import ABC, abstractmethod
#common contract (abstraction)
class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass
#Stripe implementation
class StripePayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing Stripe payment: {amount}")
#Razorpay implementation
class RazorpayPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing Razorpay payment: {amount}")
#OrderService depends on abstraction, not a specific provider
class OrderService:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def checkout(self, amount):
        self.payment_method.process(amount)
payment = RazorpayPayment()
#we can change RazorpayPayment() to StripePayment()
#or PayPalPayment() without modifying OrderService.
#the client knows WHAT to do, not HOW it is done.
#__________________________________________________________________
#...................................................................