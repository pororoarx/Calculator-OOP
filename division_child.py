from division import Division
import math

class ChildDivision(Division):
    def square_root(self, number_1, number_2):
        try:
            number_1 = float(number_1)
            number_2 = float(number_2)
        
            if number_2 == 0:
                raise ZeroDivisionError("Invalid inpput. Division by zero error.")
            
            result = number_1 / number_2
            print("Result: ", result)

            square_root = math.sqrt(result)
            print("The square root of the result is: ", square_root)

        except ValueError:
            print("Invalid input")
        except ZeroDivisionError as error:
            print(error)