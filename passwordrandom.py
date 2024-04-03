import random

chars=  "abcdefghijklmnopqrstuvwxyz1234567890@#!$%"

cont =""

for i in range(7):
    cont += random.choice(chars)

print(f"your password is: {cont}")