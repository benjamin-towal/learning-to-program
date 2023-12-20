'''
The logic definition of the program:
1. The program prompt the user to enter integers 1 to 6
2. The intergers are linked to each day of the week
3. The user will also be asked to enter the number of days since the today's day
4. The program will used the integer 
   a. today's date
   b. number of days elapsed
   c. calculate the future day
Test Case 1:
Develop the formula of future day
n0 = Sunday
n1 = Monday
n2 = Tuesday
n3 = Wednesday
n4 = Thursday
n5 = Friday
n6 = Saturday
future date = (n1 + n)%7 
n1 = first day
n = number of days elapsed

Terminal Output
Enter today's day:1
Enter the number of days elapshed since today:3
Today is Monday and the future day is Thursday
'''

today_day = eval(input("Enter today's day:"))

num_days_ahead = eval(input("Enter the number of days elapshed since today:"))

future_day_cal = (today_day + num_days_ahead) % 7

if today_day == 0:
    day = "Sunday"

elif today_day == 1:
    day = "Monday"

elif today_day == 2:
    day = "Tuesday"

elif today_day == 3:
    day = "Wednesay"

elif today_day == 4:
    day = "Thursday"

elif today_day == 5:
    day = "Friday"

elif today_day == 6:
    day = "Saturday"


if future_day_cal == 0:
    future_day = "Sunday"

elif future_day_cal == 1:
    future_day = "Monday"

elif future_day_cal == 2:
    future_day = "Tuesday"

elif future_day_cal == 3:
    future_day = "Wednesay"

elif future_day_cal == 4:
    future_day = "Thursday"

elif future_day_cal == 5:
    future_day = "Friday"

elif future_day_cal == 6:
    future_day = "Saturday"

print("Today is", day, "and the future day is", future_day)
