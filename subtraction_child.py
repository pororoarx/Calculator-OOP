from subtraction import Subtraction

class ChildSubtract(Subtraction):
    def subtraction_operation(self, number_1, number_2):
        super().subtraction_operation(number_1, number_2)

    def absolute_value(self, number_1, number_2):
        absolute = abs (number_1 - number_2)
        print("Absolute value: ", absolute)
