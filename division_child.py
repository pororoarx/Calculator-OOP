from division import Division
import math

class ChildDivision(Division):
    def square_root(self, number_1, number_2):
        number_1 = float(number_1)
        number_2 = float(number_2)
        
        result = number_1 / number_2
        print("Absolute value: ", result)

        square_root = math.sqrt(result)
        print("The square root of the result is: ", square_root)