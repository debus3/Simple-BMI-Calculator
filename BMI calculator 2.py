gender = input("What's your gender? (M/F) ")
age = input("How old are you? ")
height = input("What's your height? (in cm) ")
weight = input("What's your weight? (in kg)")

a = float(age)
x = float(weight)
y1 = float(height)
y = float(height)/100
z1=x/(y**2)
z=round(z1,2)

if gender == "M":
    kcal1 = round((1.3*(66 + (13.7*x) + (5*y1) - (6.76*a)))-300,0)
else:
    kcal1 = round((1.3*(655 + (9.6*x) + (1.8*y1) - (4.7*a)))-300,0)

if gender == "M":
    kcal2 = round((1.3*(66 + (13.7*x) + (5*y1) - (6.76*a)))+300,0)
else:
    kcal2 = round((1.3*(655 + (9.6*x) + (1.8*y1) - (4.7*a)))+300,0)

print("\nYour BMI is {}" .format(z))
print("Correct BMI should be between 18.5 and 24.9")

if z > 24.9:
    print("\nYou are a little bit overweight, try healthier diet and excercising!\n\nFor healthy weight reduction you should eat about {} kcal a day" .format(kcal1))
          
elif z <24.9 and z >= 18.5:
    print("\nYour weight is ok, congratulations!")

else:
    print("\nYou are underweight, try gaining some kilograms!\n\nFor healthy weight gain you should eat about {} kcal a day" .format(kcal2))