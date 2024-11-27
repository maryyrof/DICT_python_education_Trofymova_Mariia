def create_empty_field():
    """
    Створює порожнє ігрове поле 3x3, заповнене символами '_'.

    Returns:
        list: Список списків, що представляє ігрове поле.
    """
    return [['_' for _ in range(3)] for _ in range(3)]

def print_field(field):
    """
    Виводить ігрове поле 3x3 на екран.

    Args:
        field (list): Двовимірний список, що представляє ігрове поле.
    """
    print("---------")
    for row in field:
        print(f"| {' '.join(row)} |")
    print("---------")

def get_user_input():
    """
    Отримує від користувача рядок з 9 символів ('X', 'O', '_') і перевіряє його правильність.

    Returns:
        str: Коректний рядок, введений користувачем.
    """
    while True:
        user_input = input("Enter cells: ")
        if len(user_input) != 9 or not all(char in "XO_" for char in user_input):
            print("Incorrect cells format")
        else:
            return user_input

def create_field_from_input(user_input):
    """
    Створює ігрове поле з введеного користувачем рядка.

    Args:
        user_input (str): Рядок з 9 символів.

    Returns:
        list: Двовимірний список, що представляє ігрове поле.
    """
    field = []
    for i in range(0, 9, 3):
        row = [user_input[i], user_input[i + 1], user_input[i + 2]]
        field.append(row)
    return field

def check_winner(field, player):
    """
    Перевіряє, чи є у гравця виграшна комбінація (ряд, стовпець або діагональ).

    Args:
        field (list): Двовимірний список, що представляє ігрове поле.
        player (str): Символ гравця ('X' або 'O').

    Returns:
        bool: True, якщо гравець виграв, False - інше.
    """
    # Перевірка рядків, стовпців і діагоналей
    for i in range(3):
        if all(cell == player for cell in field[i]):  # Перевірка рядка
            return True
        if all(field[j][i] == player for j in range(3)):  # Перевірка стовпця
            return True
    if field[0][0] == player and field[1][1] == player and field[2][2] == player:  # Перевірка головної діагоналі
        return True
    if field[0][2] == player and field[1][1] == player and field[2][0] == player:  # Перевірка побічної діагоналі
        return True
    return False


def check_game_status(field):
    """
    Визначає статус гри: перемога, нічия, не завершена або некоректний ввід.

    Args:
        field (list): Двовимірний список, що представляє ігрове поле.

    Returns:
        str: Строка, що описує статус гри.
    """
    # Лічильник для кількості X і O
    x_count = sum(row.count('X') for row in field)
    o_count = sum(row.count('O') for row in field)

    # Перевірка на можливі помилки (різниця більше ніж 1)
    if abs(x_count - o_count) > 1:
        return "Impossible"

    # Перевірка на перемогу X чи O
    x_wins = check_winner(field, 'X')
    o_wins = check_winner(field, 'O')

    if x_wins and o_wins:
        return "Impossible"
    if x_wins:
        return "X wins"
    if o_wins:
        return "O wins"

    # Перевірка на гру, яка не завершена
    if '_' in ''.join([cell for row in field for cell in row]):
        return "Game not finished"

    # Якщо немає порожніх клітин і нема переможця, то нічия
    return "Draw"

def make_move(field, player):
    """
    Дозволяє гравцю зробити хід, перевіряючи правильність координат.

    Args:
        field (list): Двовимірний список, що представляє ігрове поле.
        player (str): Символ гравця ('X' або 'O').
    """
    while True:
        coordinates = input(f"Enter the coordinates for {player}: ").split()
        if len(coordinates) != 2 or not all(coord.isdigit() for coord in coordinates):
            print("You should enter numbers!")
            continue
        row, col = map(int, coordinates)
        row -= 1
        col -= 1
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Coordinates should be from 1 to 3!")
            continue
        if field[row][col] != '_':
            print("This cell is occupied! Choose another one!")
            continue
        field[row][col] = player
        break

def play_tic_tac_toe():
    """Основний цикл, запускає гру"""
    field = create_empty_field()
    current_player = 'X'
    while True:
        print_field(field)
        make_move(field, current_player)
        game_status = check_game_status(field)
        if game_status != "Game not finished":
            print_field(field)
            print(game_status)
            break
        current_player = 'O' if current_player == 'X' else 'X'


play_tic_tac_toe()



