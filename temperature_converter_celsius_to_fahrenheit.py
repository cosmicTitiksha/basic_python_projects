def c_to_f(celsius):
  return f"Gabriel says: It's {(9/5*celsius)+32} degrees Fahrenheit..."

def f_to_c(fahrenheit):
  return f"It's {5/9*(fahrenheit-32)} degrees Celsius, will you visit Sweden, Anders' homeland?"

print("Celsius <-> Fahrenheit Converter".center(130,'_'))

query = input("Want the conversion to (C/F)? : ").upper()

if query == 'C':
  entry = float(input("Enter the temperature to convert: "))
  print(f_to_c(entry))

elif query == 'F':
  entry = float(input("Enter the temperature to convert: "))
  print(c_to_f(entry))

else:
  print("Hey buddy, be serious!!!")