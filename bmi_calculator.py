print("Welcome to BMI Calculator!".center(130,'_'))
weight = float(input('Enter your weight in kilograms : '))
height = float(input('Enter your height in metres : '))
bmi = weight/(height**2)

if bmi > 0 and bmi < 18.5 : 
  result = 'Underweight'
elif bmi >= 18.5 and bmi <= 24.9 :
  result = 'Normal Weight'
elif bmi >= 25 and bmi <= 29.9 :
  result = 'Overweight'
elif bmi > 30:
  result = 'Obese'

print(f"Your BMI is {bmi} and you are {result}")