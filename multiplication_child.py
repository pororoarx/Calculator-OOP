from multiplication import Multiplication

class ChildMultiplication(Multiplication):
    def exponent(self, number_1, number_2):
        number_1 = float(number_1)
        number_2 = float(number_2)
        result = number_1 ** number_2
        print("Exponentiation value: ", result)
        