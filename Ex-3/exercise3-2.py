height = float(input("Enter you height in m: "))
weight = float(input("Enter you weight in m: "))

BMI = weight / ( height ** 2)

if BMI <= 18.5:
    print(f"Your BMI is {BMI}you are underweight")
elif 18.5 < BMI <= 25:
    print(f"Your BMI is {BMI}you are normal weight")
elif 25 < BMI <= 30:
    print(f"Your BMI is {BMI}you are normal overweight")
elif 30 < BMI <= 35:
    print(f"Your BMI is {BMI}you are normal obese")
else:
    print(f"Your BMI is {BMI}you are clinically obese")