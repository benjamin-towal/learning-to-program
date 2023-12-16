# Import math library to use squareroot function
import math


def lab_4_1():
    a, b, c = eval(input('Enter a, b, c: '))

    discriminant = (b**2) - (4 * a * c)

    if discriminant == 0:
        roots_a = roots_a = ((-b) + math.sqrt(discriminant))/(2*a)
        roots_b = ((-b) - math.sqrt(discriminant))/(2*a)
        roots_a = roots_b
        print("The root are:", roots_a)

    elif discriminant > 0:
        roots_a = roots_a = ((-b) + math.sqrt(discriminant))/(2*a)
        roots_b = ((-b) - math.sqrt(discriminant))/(2*a)
        print("The root are:", roots_a, roots_b)

    else:
        print("The equation has no real root")


lab_4_1()
