import requests

def get_exchange_rates(base_currency):
    """
    Отримує курси валют для заданої базової валюти з сайту FloatRates.
    """
    url = f"https://www.floatrates.com/daily/{base_currency}.json"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def initialize_cache(rates):
    """
    Ініціалізує кеш з курсами USD і EUR, якщо вони є в наявності.
    """
    cache = {}
    for currency in ['usd', 'eur']:
        if currency in rates:
            cache[currency] = rates[currency]['rate']
    return cache

def get_target_currency():
    """
    Запитує у користувача код валюти призначення.
    """
    return input("Enter target currency code (or press Enter to exit): ").lower()

def get_amount():
    """
    Запитує у користувача суму для конвертації.
    """
    while True:
        try:
            return float(input("Enter the amount of money: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def convert_currency(amount, rate, target_currency):
    """
    Виконує конвертацію валюти та виводить результат.
    """
    converted_amount = round(amount * rate, 2)
    print(f"You received {converted_amount} {target_currency.upper()}.")

def currency_converter():
    """
    Основна функція програми для конвертації валют.
    """
    base_currency = input("Enter your base currency code: ").lower()
    rates = get_exchange_rates(base_currency)
    if not rates:
        return

    cache = initialize_cache(rates)

    while True:
        target_currency = get_target_currency()
        if not target_currency:
            break

        amount = get_amount()

        print("Checking the cache...")

        if target_currency in cache:
            print("It is in the cache!")
            rate = cache[target_currency]
        else:
            print("Sorry, but it is not in the cache!")
            if target_currency in rates:
                rate = rates[target_currency]['rate']
                cache[target_currency] = rate
            else:
                print(f"Exchange rate for {target_currency.upper()} is not available.")
                continue

        convert_currency(amount, rate, target_currency)


currency_converter()
