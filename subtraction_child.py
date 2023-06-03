from subtraction import Subtraction

class ChildSubtract(Subtraction):
    def subtract_absolute(self, number_1, number_2):
        result = number_1 - number_2
        print("Absolute value: ", result)