import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lấy lựa chọn từ user
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

game_images = [rock, paper, scissors]

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

print(f"computer chose:")
print(game_images[computer_choice])

#logic tro choi
 #kiem tra input hop le
if user_choice >= 3 or user_choice < 0:
    print('you type an invalid number! ')
 #kiem tra hoa
if user_choice == computer_choice:
    print('its draw!')
 #kiem tra thang
if user_choice == 0 and computer_choice == 2:
    print('you win!')
if user_choice > computer_choice:
    print('you win!')
 #kiem tra thua
if user_choice == 2 and computer_choice == 0:
    print('you lose')
if user_choice < computer_choice:
    print('you lose')

