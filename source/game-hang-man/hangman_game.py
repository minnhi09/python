import random
import hangman_art


print(hangman_art.logo)

word_list = ['fairy','bloom','kingdom','echo','wander','velvet','luminuos','spark']

choosen_word = random.choice(word_list)
print(choosen_word)


placeholder = ''
word_length = len(choosen_word)
for space in range(word_length):
    placeholder += '_'
print(placeholder)

#while loop, game_over = False thi chay code, if '_' not in display thi game_over = true
game_over = False
correct_letter = []
lives = 6

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input('Guess a letter: ').lower()

    if guess in correct_letter:
        print(f'you\'ve already guessed {guess} ')
    
    display = ''
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += '_'
    print(display)

    if guess not in choosen_word:
        lives -= 1
        print('you lose a live for guess a wrong letter')
        if lives == 0:
            game_over == True
            print(f"**********************IT WAS {choosen_word}! YOU LOSE**********************")

    print(f"Current guess: {guess}")
    print(f"Correct letters: {correct_letter}")
    print(f"Display: {display}")
    
    print(hangman_art.stages[lives])

    if '_' not in display:
        game_over = True
        print('==================================YOU WIN!===================================')


