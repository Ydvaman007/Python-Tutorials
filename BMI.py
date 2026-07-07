name = input("Enter your Name here please:-")

# To calculate the Body mass Index We must know about the height(in meters) and Weight(kg)

#Weight input 
weight = float(input("Enter Your weight(in Kilograms) here:-"))

# Height input
height = float(input("Enter Your height (in meters) here:-"))



# BMI calculation

# BMI formula = weight/height
bmi = weight / height**2

print(f"BMI of {name} is = ",bmi)