def welcome():
    print("Welcome to this simple area calculator program")
    print("Enter A to calcuate area of Square:")
    print("Enter B to calcuate area of Triangle:")


def options():
    user_select_option_a = "A"
    user_select_option_b = "B"
    options = str.upper(
        input("Enter option find your area of the shapes: "))
    if options == user_select_option_a:
        area_of_square()
    elif options == user_select_option_b:
        area_of_triangle()


def area_of_square():
    len_of_side_a = eval(input('What is the length of side a of square ? '))
    len_of_side_b = eval(input('What is the length of side b of square ? '))
    area = (len_of_side_a) * (len_of_side_b)
    print(area)


def area_of_triangle():
    len_of_base_a = eval(input('What is the base of the triangle? '))
    len_of_height_b = eval(input('What is height of the triagle? '))
    area = (len_of_base_a * len_of_height_b)/2
    print("The area of the triangle is :", area)


# Call your function to perform the required tasks
welcome()
print()
options()
