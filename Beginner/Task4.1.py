#Take user input for the height and weight
height = float(input("Enter the height in meters : "))
weight = float(input("Enter the weight in kilograms : "))

#Calculate the BMI
BMI = weight/(height*height)

#Categorise the BMI based On the user input
if BMI>=30 :
    print("Obesity")
elif BMI>=25 :
    print("Overweight")
elif BMI>=18.5 :
    print("Normal")
else:
    print("Underweight")