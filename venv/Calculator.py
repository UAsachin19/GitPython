class Calculator:
    num = 100
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("My first method")
        print(20+11)

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2, 3)
obj.getData()
print(obj.summation())
