class Subtraction:
    def subtraction_operation(self, number_1, number_2):
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

            # calculate the difference and print the result
            result = number_1 - number_2
            print("\033[95m\nThe difference is:", result, "\033[0m")
              
        # if the user entered an invalid response, catch the exception and print an error message
        except ValueError:
            print("\033[91mInvalid input \033[0m")
