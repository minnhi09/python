import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

so_tu = int(input('how many letter do you want in your password?\n'))
so_kytu = int(input('how many symbols do you want?\n'))
so_so = int(input('how many munber do you want?\n'))

password_list = []

for char in range(0,so_tu):
    password_list.append(random.choice(letters))
for char in range(0, so_kytu):
    password_list.append(random.choice(symbols))
for char in range(0,so_so):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
 
password = "" 

for char in password_list:
    password += char

print(f'your password is: ${password}')