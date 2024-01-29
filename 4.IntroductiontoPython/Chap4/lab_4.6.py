''' 
The logic definition of the program:
1.The program will prompts the user to enter the input of the measurment
2.Calculate the inputs with the sturdy measurment
3.The calculation will link to your final program run
Terminal Output;
Enter the weight in pounds: 140
Enter feet: 5
Enter inches: 10
BMI is 20.087702275404553
You are Normal
'''


weight = eval(input('Enter the weight in pounds: '))
height = eval(input('Enter feet: '))
inches = eval(input('Enter inches: '))
weightInKilogram = weight * 0.45359237
heightInMeters = height * 0.3048
heightInInches = inches * 0.0254
bmi = (weightInKilogram / ((heightInMeters + heightInInches * heightInInches))/2)
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("Underwieght")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
