import math
def days():
user_select_monday_1 = 1
monday = str(input("Enter today's day: "))
if monday == user_select_monday_1:
    print(" ")

number_of_days = eval(input("Enter the number of day elapsed since today: "))
cal_day = (3 - 2)
if cal_day > 6:
    futur = (3 - 2)
    print("Today is Monday and the future day is Thursday")
