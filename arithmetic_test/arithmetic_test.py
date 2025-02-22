import random


def generate_task_level_1():
    """
    Генерує арифметичне завдання для рівня 1, яке включає прості операції (додавання, віднімання, множення) з числами від 2 до 9.

    Returns:
        tuple: Параметри:
            task (str): Завдання у вигляді рядка (наприклад, "3 + 4").
            correct_answer (int): Правильна відповідь на завдання.
    """
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    task = f"{num1} {operation} {num2}"

    # Обчислюємо правильну відповідь
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return task, correct_answer


def generate_task_level_2():
    """
    Генерує завдання для рівня 2, яке вимагає зведення числа в квадрат з чисел від 11 до 29.

    Returns:
        tuple: Параметри:
            task (str): Завдання у вигляді рядка (наприклад, "15").
            correct_answer (int): Правильна відповідь на завдання (квадрат числа).
    """
    num = random.randint(11, 29)
    task = f"{num}"
    correct_answer = num ** 2
    return task, correct_answer


def is_valid_input(user_input):
    """
    Перевіряє, чи є введене значення правильним числом (ціле число, в тому числі від'ємне).

    Args:
        user_input (str): Введене значення, яке потрібно перевірити.

    Returns:
        bool: True, якщо введене значення є числом, інакше False.
    """
    if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
        return True
    return False



def main():
    """
    Головна функція програми, яка виконує весь тест.
    Запитує користувача про рівень складності, генерує завдання, перевіряє відповіді,
    надає результат та пропонує зберегти його у файл.
    """
    level = None
    while level not in [1, 2]:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        level_input = input("> ").strip()

        if level_input == "1":
            level = 1
        elif level_input == "2":
            level = 2
        else:
            print("Incorrect format. Please enter 1 or 2.")

    correct_answers = 0

    # Задаємо 5 завдань
    for i in range(5):
        task = ""
        correct_answer = None

        if level == 1:
            task, correct_answer = generate_task_level_1()
        elif level == 2:
            task, correct_answer = generate_task_level_2()

        print(task)

        while True:
            user_answer = input("> ").strip()

            # Перевірка на правильний формат введення
            if not is_valid_input(user_answer):
                print("Wrong format! Try again.")
                continue

            user_answer = int(user_answer)

            # Перевірка відповіді
            if user_answer == correct_answer:
                print("Right!")
                correct_answers += 1
                break
            else:
                print("Wrong!")
                break

    print(f"Your mark is {correct_answers}/5.")

    # Запит на збереження результатів в файл
    while True:
        print("Would you like to save your result to the file? Enter yes or no.")
        save_result = input("> ").strip().lower()

        if save_result in ["yes", "y", "yes", "y"]:
            name = input("What is your name?\n> ").strip()
            level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"
            with open("results.txt", "a") as file:
                file.write(f"{name}: {correct_answers}/5 in level {level} ({level_description}).\n")
            print('The results are saved in "results.txt".')
            break
        elif save_result == "no":
            break
        else:
            print("Incorrect input. Please enter 'yes' or 'no'.")


main()