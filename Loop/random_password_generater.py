import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
# easy way to generate password
# password = ""

# for i in range(0,nr_letters):
#     password += random.choice(letters)

# for i in range(0,nr_numbers):
#     password += random.choice(numbers)

# for i in range(0,nr_symbols):
#     password += random.choice(symbols)
# print(password)

# hard way to generate password
password_list = []

for i in range(0,nr_letters):
    password_list += random.choice(letters)

for i in range(0,nr_numbers):
    password_list += random.choice(numbers)

for i in range(0,nr_symbols):
    password_list += random.choice(symbols)
print(password_list)
random.shuffle(password_list)
# bad practice
# password = ""
# for char in password_list:
#     password += char
# print(f"Your password is: {password}")

# good practice
password = "".join(password_list)
print(f"Your password is: {password}")
