def welcome():
    print("welcome to the simple caculator program")


def options():
    option = str(input("[a] Enter option (a) to find the area: "))
if option == "a":
      area_of_square()
else:
        welcome()
        options()

    def area_of_square():
        len_of_side_a = eval(input("What is the lenght of side a? "))
        len_of_side_b = eval(input("What is the lenght of side b? "))
        area = len_of_side_a * len_of_side_b
        return area


print(welcome())
print(options())
print(area_of_square())
