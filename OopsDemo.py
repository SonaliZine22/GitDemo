
class Calculator:
    num=100

    def __init__(self, a, b):
        self.firstNumber=a
        self.secondNumber = b

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(3, 5)
print(obj.summation())
obj1 = Calculator(5, 5)
print(obj1.summation())


