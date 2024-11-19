import random

def add_friends():
    """Збирає імена друзів та повертає словник та їх початкові рахунки"""
    while True:
        num_of_friends = input("Enter the number of friends joining (including you), each on a new line: ")
        if num_of_friends.isnumeric():
            num_friends = int(num_of_friends)
            break
        else:
            # Якщо введено не число, виводиться повідомлення
            print("Please, enter a number!")
    if num_friends <= 0:
        print("No one is joining for the party")
        return {}

    # Створення списка, в якому кожен друг на початку має рахунок 0
    friends = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_friends):
        name = input("> ")
        friends[name] = 0
    return friends


def calculate_the_bill(friends):
    """Розраховує для кожного друга рівну частинку від загального рахунку"""
    if not friends:
        return None

    # Введення повної суми рахунку
    total_amount = float(input("Enter the total amount: "))

    # Розподіляє суму між усіма друзями
    divided_amount = round(total_amount / len(friends), 2)
    for friend in friends:
        friends[friend] = divided_amount


def choose_lucky_friend(friends):
    """Випадково вибирає щасливчика, який не буде платити"""
    if not friends:
        return None

    # Запитує, чи хоче користувач вибрати "щасливчика"
    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')

    if lucky_choice.lower() == "yes":
        lucky_choice = random.choice(list(friends.keys()))
        print(f"{lucky_choice} is the lucky one!")
        return lucky_choice
    else:
        print("No one is going to be lucky")
        return


def current_the_bill(friends, lucky_human):
    """Рахує рахунок для кожного друга, окрім щасливчика"""
    if not friends:
        return

    if lucky_person:
        # Перерахунок суми для n-1 друзів
        split_amount = round(sum(friends.values()) / (len(friends) - 1), 2)
        for friend in friends:
            if lucky_human and friend != lucky_person:
                friends[friend] = split_amount
            else:
                friends[friend] = 0
    print(friends)


friends_dict = add_friends()
calculate_the_bill(friends_dict)
lucky_person = choose_lucky_friend(friends_dict)
current_the_bill(friends_dict, lucky_person)
