import random

chars=  "abcdefghijklmnopqrstuvwxyz1234567890@#!$%"

password =""

for i in range(7):
    password += random.choice(chars)

print(f"your password is: {password}")