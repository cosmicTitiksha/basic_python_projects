import random

sequence = 'abcdefghijklmnopqrstuvwxyxABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_-+|:;>.,<?/'
number = int(input("How many characters do you need in your password? : "))

password = ''.join(random.choices(sequence, k=number))  # Join list into a string
print("Generated Password:", password)
