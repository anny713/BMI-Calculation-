print("This program is t0 calculate the BMI  of an individual\n")
name = input("Enter your name : ")
weight = float(input("Enter your weight: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 25:
    print(f"{name} is underweight by {bmi} BMI")
else:
    print(f"{name} is overweight by {bmi} BMI")