# import Addition class
from addition import Addition

# create a new class
class ChildAddition(Addition):
    def add(self, number_1, number_2):
        sum = number_1 + number_2
        return sum
    