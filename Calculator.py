def getdata():
    print("My first method")
    print(20 + 11)


class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)
print(obj.summation())
