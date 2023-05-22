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

        # if user chooses addition
        if chosen_operation == "1":
            # ask the user to enter two numbers
            number_1 = input("\033[38;5;214mEnter your first number: \033[0m")
            number_2 = input("\033[38;5;214mEnter your second number: \033[0m")

            add = Addition()
            add.addition_operation(number_1, number_2)

        # if user chooses subtraction
        elif chosen_operation == "2":
            # ask the user to enter two numbers
            number_1 = input("\033[38;5;214mEnter your first number: \033[0m")
            number_2 = input("\033[38;5;214mEnter your second number: \033[0m")

            subtract = Subtraction()
            subtract.subtraction_operation(number_1, number_2)


