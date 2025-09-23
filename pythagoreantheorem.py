# TODO create class PythagoreanTheorem
import math

if __name__ == "__main__":
    # create PythagoreanTheorem below this
    pass

class PythagoreanTheorem:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def hypotenuse(self):
        return math.sqrt(self.a**2+self.b**2)
