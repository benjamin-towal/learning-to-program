
import math

# Assign our input values to the variables (a, b, c, d, e, f)
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f:"))

num_calculation = (a * d) - (b * c)

if num_calculation < 0:
    val_x = ((e * d) - (b * f))/((a * d) - (b * c))
    val_y = ((a * f) - (e * c))/((a * d) - (b * c))
    print("x is ", val_x, "and y is ", val_y)
else:
    print("The equation has no solution")
