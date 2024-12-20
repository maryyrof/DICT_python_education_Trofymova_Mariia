class CoffeeMachine:
    def __init__(self):
        """
        Ініціалізує об'єкт кавомашини з початковими запасами.
        Ресурси:
        - water (int): Кількість води в мл.
        - milk (int): Кількість молока в мл.
        - coffee_beans (int): Кількість кавових зерен у грамах.
        - cups (int): Кількість одноразових стаканчиків.
        - money (int): Кількість грошей у гривнях.
        """
        self.water = 400  # ml
        self.milk = 540  # ml
        self.coffee_beans = 120  # g
        self.cups = 9  # disposable cups
        self.money = 550  # грн

    def remaining(self):
        """
        Виводить поточний стан кавомашини.
        Не приймає аргументів.
        Returns:
            None.
        """
        print(
            f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee_beans} of coffee beans\n{self.cups} of disposable cups\n{self.money} of money")

    def fill(self):
        """
        Запитує у користувача, скільки ресурсів додати, і додає їх до запасів кавомашини.
        Не приймає аргументів.
        Returns:
            None.
        """
        water = int(input("Write how many ml of water you want to add:\n>"))
        milk = int(input("Write how many ml of milk you want to add:\n>"))
        coffee_beans = int(input("Write how many grams of coffee beans you want to add:\n>"))
        cups = int(input("Write how many disposable cups you want to add:\n>"))

        self.water += water
        self.milk += milk
        self.coffee_beans += coffee_beans
        self.cups += cups


    def take(self):
        """
        Забирає всі гроші з кавомашини.
        Не приймає аргументів.
        Returns:
            None.
        """
        print(f"I gave you {self.money}")
        self.money = 0

    def buy(self):
        """
        Запитує у користувача, який тип напою приготувати, і перевіряє наявність ресурсів.
        Напої:
        - 1: еспресо
        - 2: латте
        - 3: капучино
        - back: повернення до головного меню
        Не приймає аргументів.
        Returns:
            None.
        """
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:\n>")
        choice = input()

        if choice == '1':
            self.making_coffee(250, 0, 16, 4)
        elif choice == '2':
            self.making_coffee(350, 75, 20, 7)
        elif choice == '3':
            self.making_coffee(200, 100, 12, 6)
        elif choice == 'back':
            return

    def making_coffee(self, water_need, milk_need, beans_need, price):
        """
        Перевіряє наявність ресурсів і готує каву, якщо ресурсів достатньо.

        Args:
        - water_need (int): Кількість води, необхідна для напою (мл).
        - milk_need (int): Кількість молока, необхідна для напою (мл).
        - beans_need (int): Кількість кавових зерен, необхідна для напою (г).
        - price (int): Вартість напою в гривнях.

        Returns:
            None.
        """
        if self.water >= water_need and self.milk >= milk_need and self.coffee_beans >= beans_need and self.cups >= 1:
            self.water -= water_need
            self.milk -= milk_need
            self.coffee_beans -= beans_need
            self.cups -= 1
            self.money += price
            print(f"I have enough resources, making you a coffee!")
        else:
            print(f"Sorry, not enough water!")

    def start(self):
        """
        Запускає головний цикл роботи кавомашини, що дозволяє користувачу вибирати дії.
        Доступні дії:
            - buy: придбати напій
            - fill: додати ресурси
            - take: вилучити гроші
            - remaining: показати стан ресурсів
            - exit: вимкнути кавомашину
        Returns:
            None.
        """
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n>")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                print("Turning off the coffee machine.")
                break

# Створення кавомашини та запуск її роботи
machine = CoffeeMachine()
machine.start()