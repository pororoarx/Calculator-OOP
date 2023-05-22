# import four different operations
from addition import Addition
from subtraction import Subtraction
from multiplication import Multiplication
from division import Division
from display_operations import OperationsDisplay

# define a function called calculator
def calculator():
    # perform a while loop until the user decided to exit the loop
    while True:
        # ask user to enter an operation
        # print the operations that users can pick from
        print("\033[38;5;125m1. Addition\n\033[38;5;205m2. Subtraction\n\033[38;5;218m3. Multiplication\n\033[38;5;225m4. Division")
        # reset to default color
        print("\033[0m")
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

        # if user chooses multiplication
        elif chosen_operation == "3":
            # ask the user to enter two numbers
            number_1 = input("\033[38;5;214mEnter your first number: \033[0m")
            number_2 = input("\033[38;5;214mEnter your second number: \033[0m")

            multiply = Multiplication()
            multiply.multiplication_operation(number_1, number_2)

        # if user chooses division
        elif chosen_operation == "4":
            while True:
            # ask the user to enter two numbers
                number_1 = input("\033[38;5;214mEnter your first number: \033[0m")
                number_2 = input("\033[38;5;214mEnter your second number: \033[0m")

                divide = Division()
                divide.division_operation(number_1, number_2)
        
        # if user entered an invalid operation,
        else:
            # print an error message
            print("\033[91mInvalid input \033[0m")

        # ask user if they want to solve again
        new_computation = str(input("\033[38;5;156m\nWould you like to solve again? (YES/NO): \033[0m"))

        # if the user answered yes,
        if new_computation.upper() == "YES":
            # call the calculator function to repeat the process
            calculator()

        # if the user answered no,
        elif new_computation.upper() == "NO":
            # print thank you and exit the program
            print("\n\033[34mThank you! \033[0m")
            break

        # if user entered an invalid response, print an error message
        else:
            print("Invalid response. Kindly run it again.")
            break


        # break out of the loop
        break
    



