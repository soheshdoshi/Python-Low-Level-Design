#The Interface Segregation Principle states that “No client should be forced to depend on methods it does not use”.

class SMS:
    def make_sms(self):
        print("sms class")


class CALL:
    def make_call(self):
        print("call class")



class Communication(SMS, CALL):
    # if i don't want to implement call i will remove from inheritance
    def make_sms(self):
        print("make sms ")
