'''
Here Im going to ask the program to find the true or faulse
STEPS:
      1. Creat the suitable variable that prompts the user to enter an integer
      2. If the number is a multiple of 5 the program display the result HiFive
      3. If the number is divisible by 2, the program disply displays HiEven
Program Run;
Enter an integer: Integer 
HiFive or HiEven      
'''

number = eval(input('Enter an integer: '))
if number % 5 == 0:
    print("HiFive")
if number % 2 == 0:
    print("HiEven")
if number % 2 != 0:
    print("not equal too")


print()
