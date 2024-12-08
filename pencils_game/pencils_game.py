import random

def number_of_pencils(count):
    """
    Відображає поточну кількість олівців у грі.

    Args:
        count: Кількість олівців, які залишилися.
    """
    print("|" * count)

def initial_quantity():
    """
    Отримує від користувача початкову кількість олівців для гри.

    Returns:
        int: Початкова кількість олівців.
    """
    while True:
        pencils_str = input("How many pencils would you like to use:\n> ")
        if pencils_str.isdigit():
            pencils = int(pencils_str)
            if pencils > 0:
                return pencils
            else:
                print("The number of pencils should be a positive integer.")
        else:
            print("Please enter a valid number.")

def select_the_first_player(player_1, player_2):
    """Вибирає, хто з двох гравців ходитиме першим.

    Args:
        player_1: Ім'я першого гравця.
        player_2: Ім'я другого гравця.

    Returns:
        str: Ім'я гравця, який ходитиме першим.
    """
    while True:
        first_player = input(f"Who will be the first ({player_1}, {player_2}):\n> ")
        if first_player in {player_1, player_2}:
            return first_player
        else:
            print(f"Choose between '{player_1}' and '{player_2}'")

def gamer_move(most_pencils):
    """
    Отримує від користувача кількість олівців, які він хоче забрати.

    Args:
        most_pencils: Максимальна кількість олівців, яку можна забрати.

    Returns:
        int: Кількість олівців, яку забрав гравець.
    """
    while True:
        move_str = input("Enter the number of pencils to take (1, 2, or 3):\n> ")
        if move_str.isdigit():
            move = int(move_str)
            if 1 <= move <= 3 and move <= most_pencils:
                return move
            else:
                print("Too many pencils were taken!")


def computer_move(pencils):
    """Хід комп'ютера.

    Args:
        pencils: Поточна кількість олівців на столі.

    Returns:
        int: Кількість олівців, яку забрав комп'ютер.
    """
    random_choice = random.randint(1, min(3, pencils))  # Генерує випадковий вибір наперед
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1

    # Якщо жодна умова не спрацювала, повертає випадковий вибір
    return random_choice

def play_pencils_game():
    """Основна логіка гри.Запускає гру в олівці."""
    gamer_one, gamer_two = "Mariya", "Computer"
    pencils = initial_quantity()

    if select_the_first_player(gamer_one, gamer_two) == gamer_one:
        actual_player = gamer_one
    else:
        actual_player = gamer_two

    while pencils > 0:
        print(f"{actual_player}'s turn!")

        if actual_player == gamer_one:
            move = gamer_move(pencils)
        else:
            move = computer_move(pencils)

        if actual_player == gamer_two:
            print(move)

        pencils -= move
        if pencils > 0:
            number_of_pencils(pencils)

        if actual_player == gamer_one:
            actual_player = gamer_two
        else:
            actual_player = gamer_one

    print(f"{actual_player} won!")

play_pencils_game()

