import random

print("HANGMAN")

words = ['python', 'java', 'javascript', 'php']   #список слів

def get_user_guess(guessed_letters):
    """Отримує від користувача одну літеру,
    та перевіряє чи правильне введення та чи є ця літера у слові"""
    user_guess = input("Input a letter: ").strip()
    if len(user_guess) != 1 or not user_guess.isalpha() or not user_guess.islower():
        print("Please enter a single lowercase English letter.")
        return None
    if user_guess in guessed_letters:
        print("You've already guessed this letter.")
        return None
    return user_guess

def update_showed_word(secret_word, showed_word, user_guess):
    """Оновлює слово, підставляючи вгадані літери."""
    new_showed_word = ""
    for i in range(len(secret_word)):
        if secret_word[i] == user_guess or showed_word[i] != '-':
            new_showed_word += secret_word[i]
        else:
            new_showed_word += '-'
    return new_showed_word

def play_game():
    """Вибирає випадкове слово та дозволяє користувачу вгадувати літери,
    поки не вичерпаються всі життя або поки не буде вгадане слово."""
    secret_word = random.choice(words)  #вибір випадкового слова зі списку
    showed_word = "-" * len(secret_word)
    print(showed_word)

    lives = 8
    guessed_letters = set()

    while lives > 0:
        user_guess = get_user_guess(guessed_letters)
        if not user_guess:
            continue

        guessed_letters.add(user_guess)

        if user_guess in secret_word:   #перевіряє чи вгадана літера є у слові
            showed_word = update_showed_word(secret_word, showed_word, user_guess)
            print(showed_word)
            if showed_word == secret_word:   #перевірка на виграш
                print("You guessed the word!")
                print("You survived!")
                return
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

    print("You lost!")

while True:
    user_choice = input("Type 'play' to play the game, 'exit' to quit: ").strip().lower()
    if user_choice == 'play':
        play_game()
    elif user_choice == 'exit':
        break
    else:
        print("Invalid input. Please try again.")
