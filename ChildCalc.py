from Calculator import Calculator


class ChildCalc(Calculator):
    num2 = 250

    def __init__(self, a, b):
        Calculator.__init__(self, a, b)
        print("child class constructor")
        name = input("Give me your name: ")
        print("Your name is " + name)

    def complete(self):
        return self.num2 + self.num + self.summation()


obj2 = ChildCalc(3, 4)
print(obj2.complete())
