# Bad Code

class Solution:
    def calculator(self, value_1, value_2, choice):
        if choice==1:
            return value_2+value_1
        elif choice==2:
            return value_2-value_1


# USING SOLID
# A class should have only one reason to change

class Solution:
    def sum(self, v1, v2):
        return v1+v2
    def subtraction(self, v1, v2):
        return v2-v1
    def calculaor(self, choice):
        if choice==1:
            return self.sum(v1, v2)
        elif choice==2:
            return self.subtraction(v1,v2)
