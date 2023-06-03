# import Addition class
from addition import Addition

# create a new class
class ChildAddition(Addition):
    def add(self):
        new_print = super().addition_operation()
        print("The answer is: ", new_print)