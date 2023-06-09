# import four different operations
from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division
from display_operations import OperationsDisplay
from subtraction_child import ChildSubtract
from addition_child import ChildAddition
from multiplication_child import ChildMultiplication
from division_child import ChildDivision

# define a function called calculator
def calculator():
    # perform a while loop until the user decided to exit the loop
    while True:
        OperationsDisplay.operations()
        chosen_operation = input("\n\033[38;5;156mChoose one of the four operations: \033[0m")

        # if user chooses addition
        if chosen_operation == "1":
            # ask the user to enter two numbers
            number_1 = input("\033[38;5;214mEnter your first number: \033[0m")
            number_2 = input("\033[38;5;214mEnter your second number: \033[0m")

            add = Addition()
            add.addition_operation(number_1, number_2)
            new_add = ChildAddition()
            new_add.add(number_1, number_2)

        # if user chooses subtraction
        elif chosen_operation == "2":
            # ask the user to enter two numbers
            number_1 = input("\033[38;5;214mEnter your first number: \033[0m")
            number_2 = input("\033[38;5;214mEnter your second number: \033[0m")

            original_sub = Subtraction()
            original_sub.subtraction_operation(number_1, number_2)
            subtract = ChildSubtract()
            subtract.absolute_value(number_1, number_2)

        # if user chooses multiplication
        elif chosen_operation == "3":
            # ask the user to enter two numbers
            number_1 = input("\033[38;5;214mEnter your first number: \033[0m")
            number_2 = input("\033[38;5;214mEnter your second number: \033[0m")

            multiply = Multiplication()
            multiply.multiplication_operation(number_1, number_2)
            exponent = ChildMultiplication()
            exponent.exponent(number_1, number_2)
            

        # if user chooses division
        elif chosen_operation == "4":
            while True:
            # ask the user to enter two numbers
                number_1 = input("\033[38;5;214mEnter your first number: \033[0m")
                number_2 = input("\033[38;5;214mEnter your second number: \033[0m")

                divide = Division()
                divide.division_operation(number_1, number_2)
                sqr_root = ChildDivision()
                sqr_root.square_root(number_1, number_2)
                
                break

        # if user entered an invalid operation,
        else:
            # print an error message
            print("\033[91mInvalid input \033[0m")

        # ask user if they want to solve again
        new_computation = input("\033[38;5;156m\nWould you like to solve again? (YES/NO): \033[0m")

        # if the user answered yes,
        if new_computation.upper() == "NO":
            # print thank you
            print("\n\033[34mThank you! \033[0m")
            break

        # if the user answered no,
        elif new_computation.upper() == "YES":
            # continue the program
            continue

        # if user entered an invalid response, print an error message
        else:
            print("Invalid response. Kindly run it again.")
            break
    

      
        

    



