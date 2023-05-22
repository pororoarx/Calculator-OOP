class Division:
    def division_operation(self, number_1, number_2):
        while True:
            # try
            try:
                # convert both inputs to float if one or both of the inputs made by user is a float
                if "." in number_1 or "." in number_2:
                    number_1 = float(number_1)
                    number_2 = float(number_2)
                    
                # otherwise, convert both inputs made by user to integers
                else:
                    number_1 = int(number_1)
                    number_2 = int(number_2)

                # calculate the quotient and print the result
                result = number_1 / number_2
                print("\033[95m\nThe quotient is:", result, "\033[0m")
                # break out of the loop
                break

            # if the user entered a division by zero error, catch the exception and print an error message
            except ZeroDivisionError:
                print("\033[91mInvalid input, division by zero error. \033[0m\n")

            # if the user entered an invalid input, catch the exception made and print an error message
            except ValueError:
                print("\033[91mInvalid input \033[0m\n")

            # perform a while loop to ask the user if they want to divide again
            while True:
                another_input = input("\033[38;5;149mWould you like to try dividing again? (YES/NO): \033[0m")
                # if yes, break out of the inner loop and repeat the division operation
                if another_input.upper() == "YES":
                    break
                # if no, return from the function and exit
                elif another_input.upper() == "NO":
                    print("\n\033[34mThank you! \033[0m")
                    return
                    
                # if user entered an invalid response, ask the user to enter either 'YES' or 'NO'
                else:
                    print("\033[91mInvalid reply. Please enter 'YES' or 'NO'\033[91m")  

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
