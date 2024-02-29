# Opdracht 1 input function
# Naam student: Ina Rommens
# Groep: ITX1

import math


def triangle():
    side_a = float(input("Enter the length of side A: "))
    side_b = float(input("Enter the length of side B: "))
    side_c = math.sqrt((side_a**2+side_b**2))

    print(f"The length of side C is {side_c}")


triangle()

