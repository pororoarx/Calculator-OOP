from subtraction import Subtraction

class ChildSubtract(Subtraction):
    def subtract_absolute(self, number_1, number_2):
        try:
            number_1 = float(number_1)
            number_2 = float(number_2)
            result = abs(number_1 - number_2)
            print("Absolute value: ", result)
        except ValueError:
            print("Invalid input")

    def absolute_value(self):
        number_1 = input("First number: ")
        number_2 = input("Second number")
        self.subtract_absolute(number_1, number_2)
