import random 

guess_words = ['shoaib', 'ahmed']
chosen_word = random.choice(guess_words)

lives = 6

stages = [
    '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
   ======
''','''
    +---+
    |   |
    O   |
   /|\  |
   /    |
   ======   
''','''
    +---+
    |   |
    O   |
   /|\  |
        |
   ======   
''','''
    +---+
    |   |
    O   |
   /|   |
        |
   ======   
''','''
    +---+
    |   |
    O   |
   /    |
        |
   ======   
''','''
    +---+
    |   |
    O   |
        |
        |
   ======   
''','''
    +---+
    |   |
        |
        |
        |
   ======   
'''
]

print(chosen_word)
display = [' _ '] * len(chosen_word)

while " _ " in display and lives > 0:
    guess = input('enter: ').lower()

    if guess in display:
        print('already there ')
        continue

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    
    if guess not in chosen_word:
        lives -= 1
        print('wrong guess')
        if lives == 0:
            print('you lose')
            exit(1)
    print(f"{' '.join(display)}")    
    print(stages[lives])

if " _ " not in display:
    print('you won!')
