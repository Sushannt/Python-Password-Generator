#Password Generator Project
from logic import ListTOString, getPassword
import random

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
generated_pass = getPassword(nr_letters, nr_numbers, nr_symbols)
easy_password = ListTOString(generated_pass)
print(f"easy password (without randomized order): {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(generated_pass)
hard_password = ListTOString(generated_pass)
print(f"hard password (with randomised order): {hard_password}")