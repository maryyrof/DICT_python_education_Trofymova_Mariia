import random
import os


def get_user_name():
    """Отримує ім'я користувача."""
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    return name


def load_user_rating(name):
    """Завантажує рейтинг користувача з файлу."""
    user_rating = 0
    if os.path.isfile("rating.txt"):
        with open("rating.txt", "r") as file:
            for line in file:
                stored_name, score = line.split()
                if stored_name == name:
                    user_rating = int(score)
                    break
    return user_rating


def get_game_options():
    """Отримує список варіантів гри від користувача з перевіркою правил."""
    while True:
        user_input = input()
        game_options = user_input.split(",") if user_input else ["rock", "paper", "scissors"]

        if len(game_options) < 3:
            print("You must enter at least three options.")
            continue
        if len(game_options) % 2 == 0:
            print("The number of options must be odd.")
            continue

        print("Okay, let's start")
        return game_options


def get_winner(player_choice, cpu_choice, choices):
    """Визначає результат гри між користувачем та комп'ютером."""
    if player_choice == cpu_choice:
        return "draw"
    index = choices.index(player_choice)
    beats = choices[index + 1:] + choices[:index]
    winning_half = beats[:len(beats) // 2]
    if cpu_choice in winning_half:
        return "win"
    return "lose"


def update_rating_file(name, user_rating):
    """Оновлює файл рейтингу."""
    lines = []
    if os.path.isfile("rating.txt"):
        with open("rating.txt", "r") as file:
            lines = file.readlines()
    updated = False
    with open("rating.txt", "w") as file:
        for line in lines:
            stored_name, score = line.split()
            if stored_name == name:
                file.write(f"{name} {user_rating}\n")
                updated = True
            else:
                file.write(line)
        if not updated:
            file.write(f"{name} {user_rating}\n")


def main():
    """Головна функція, яка запускає гру."""
    name = get_user_name()
    user_rating = load_user_rating(name)
    game_options = get_game_options()

    while True:
        user_choice = input()
        if user_choice == "!exit":
            print("Bye!")
            break
        if user_choice == "!rating":
            print(f"Your rating: {user_rating}")
            continue
        if user_choice not in game_options:
            print("Invalid input")
            continue

        computer_choice = random.choice(game_options)
        result = get_winner(user_choice, computer_choice, game_options)

        if result == "draw":
            print(f"There is a draw ({computer_choice})")
            user_rating += 50
        elif result == "win":
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_rating += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")

    update_rating_file(name, user_rating)


if __name__ == "__main__":
    main()
