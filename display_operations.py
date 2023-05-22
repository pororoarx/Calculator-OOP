# print a welcome message
class OperationsDisplay:
    def operations(self):
        # print the operations that users can pick from
        print("\033[38;5;125m1. Addition\n\033[38;5;205m2. Subtraction\n\033[38;5;218m3. Multiplication\n\033[38;5;225m4. Division")
        # reset to default color
        print("\033[0m")
