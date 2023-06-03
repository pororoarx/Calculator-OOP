from subtraction import Subtraction

class ChildSubtract(Subtraction):
    def subtract_absolute(self, number):
        number = float(number)
        result = abs(number)
        print("Absolute value: ", result)