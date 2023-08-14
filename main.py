import random

from visilica_word import word_list
from visilica_art import logo

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_lenght):
    display += '_'

while not end_of_game:
    guess = input('Угадай букву: ').lower()

    if guess in display:
        print(f'Есть такая буква - {guess}')

    for possitin in range(word_lenght):
        letter = chosen_word[possitin]

        if letter == guess:
            display[possitin] = letter

    if guess not in chosen_word:
        print(f'Буква {guess} нет, подумай еще. Ты теряешь жизнь!')

        lives -= 1
        if lives == 0:
            end_of_game = True
            print('Ты проиграл')

    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print('Победа!')

    from visilica_art import stages
    print(stages[lives])
