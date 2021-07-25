class PaymentSolution:
    def pay(self):
        print("Payment Solution")


class JioPay(PaymentSolution):
    def pay(self):
        print("Jio Payment Solution")


class PaytmPay(PaymentSolution):
    def pay(self):
        print("Paytm Payment Soltion")


p = PaytmPay()
p.pay()
