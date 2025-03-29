import math
import argparse


def calculate_diff_payments(principal, periods, interest):
    """
    Розраховує диференційовані платежі для кредиту.

    Аргументи:
    principal -- основна сума кредиту
    periods -- кількість місяців для погашення кредиту
    interest -- річна процентна ставка без знака '%'
    """
    i = interest / (12 * 100)
    total_payment = 0
    for m in range(1, periods + 1):
        dm = math.ceil((principal / periods) + i * (principal - (principal * (m - 1)) / periods))
        total_payment += dm
        print(f"Month {m}: payment is {dm}")
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")

def calculate_annuity_payment(principal, periods, interest):
    """
    Розраховує ануїтетний (щомісячний) платіж для кредиту.

    Аргументи:
    principal -- основна сума кредиту
    periods -- кількість місяців для погашення кредиту
    interest -- річна процентна ставка без знака '%'
    """
    i = interest / (12 * 100)
    annuity_payment = math.ceil(principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    overpayment = annuity_payment * periods - principal
    print(f"Your annuity payment = {annuity_payment}!")
    print(f"Overpayment = {overpayment}")

def calculate_principal(payment, periods, interest):
    """
    Розраховує основну суму кредиту на основі щомісячного платежу, кількості періодів та процентної ставки.

    Аргументи:
    payment -- сума щомісячного платежу
    periods -- кількість місяців для погашення кредиту
    interest -- річна процентна ставка без знака '%'
    """
    i = interest / (12 * 100)
    principal = math.floor(payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
    overpayment = payment * periods - principal
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {overpayment}")

def calculate_periods(principal, payment, interest):
    """
    Розраховує кількість періодів (місяців) для погашення кредиту на основі основної суми, щомісячного платежу та процентної ставки.

    Аргументи:
    principal -- основна сума кредиту
    payment -- сума щомісячного платежу
    interest -- річна процентна ставка без знака '%'
    """
    i = interest / (12 * 100)
    n = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    years = n // 12
    months = n % 12
    if years == 0:
        time = f"{months} months"
    elif months == 0:
        time = f"{years} years"
    else:
        time = f"{years} years and {months} months"
    overpayment = payment * n - principal
    print(f"It will take {time} to repay this loan!")
    print(f"Overpayment = {overpayment}")

def main():
    """
    Основна функція, яка обробляє аргументи командного рядка та викликає відповідні функції для розрахунку кредитних параметрів.
    """
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], help="Тип платежу: 'annuity' або 'diff'")
    parser.add_argument("--principal", type=float, help="Сума кредиту")
    parser.add_argument("--payment", type=float, help="Щомісячний платіж")
    parser.add_argument("--periods", type=int, help="Кількість місяців")
    parser.add_argument("--interest", type=float, help="Річна процентна ставка без знака '%'")

    args = parser.parse_args()

    if args.type not in ["annuity", "diff"]:
        print("Incorrect parameters")
        return

    if args.type == "diff":
        if not all([args.principal, args.periods, args.interest]) or args.payment:
            print("Incorrect parameters")
            return
        if args.principal < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect parameters")
            return
        calculate_diff_payments(args.principal, args.periods, args.interest)

    elif args.type == "annuity":
        if args.interest is None:
            print("Incorrect parameters")
            return
        if sum(arg is not None for arg in [args.principal, args.payment, args.periods]) != 2:
            print("Incorrect parameters")
            return
        if any(arg is not None and arg < 0 for arg in [args.principal, args.payment, args.periods, args.interest]):
            print("Incorrect parameters")
            return
        if args.principal and args.periods:
            calculate_annuity_payment(args.principal, args.periods, args.interest)
        elif args.payment and args.periods:
            calculate_principal(args.payment, args.periods, args.interest)
        elif args.principal and args.payment:
            calculate_periods(args.principal, args.payment, args.interest)

if __name__ == "__main__":
    main()

