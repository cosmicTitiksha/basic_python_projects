import random

random_num = random.randint(0,100)
print(random_num)

def make_guess(number):
  if random_num == number:
    print(f"Congrats, that's correct. In {times} tries.")
    return False
  elif number < random_num:
    print("Okay, think higher!")
  else:
    print("Yours is a bit more!")
    return True

times = 0
execution = True

while execution:
  times += 1
  number = int(input("Enter any two digit number of your choice : "))
  execution = make_guess(number)


  
