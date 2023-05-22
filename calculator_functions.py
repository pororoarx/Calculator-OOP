# import four different operations
from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division

# define a function called calculator
def calculator():
    # perform a while loop until the user decided to exit the loop
    while True:
        # ask user to enter an operation
        chosen_operation = input("\n\033[38;5;156mChoose one of the four operations: \033[0m")   