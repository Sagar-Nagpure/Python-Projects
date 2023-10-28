import random

word_list = ['apple','beautiful','potato']

lives = 6

chosen_word = random.choice(word_list)

display = []

for i in range(len(chosen_word)):
    display += '_'
print(display)

game_over = False

while not game_over:
    guessed_letter = input("\nGuess a letter = ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You Lose")

    if '_' not in display:
        game_over = True
        print("You Win")