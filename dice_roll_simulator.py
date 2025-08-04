import random

def die_roll():
  lista = [1,2,3,4,5,6]
  output = random.choice(lista)
  print(output)

begin = True
while begin:
  query = input("Do you want to roll the die? (Yes/No) : ").lower()
  if query == 'yes':
    die_roll()
  elif query == 'no':
    print("Okay! Come back to roll the dice anytime 🎲")
    break
  else:
    print("Please type 'yes' or 'no'.")