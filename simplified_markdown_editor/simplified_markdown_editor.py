def print_help():
    """Виводить список доступних форматерів і спеціальних команд."""
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line line-break")
    print("Special commands: !help !done")

def apply_format(formatter, text=None):
    """
    Застосовує вказаний формат Markdown до переданого тексту.

    Аргументи:
        formatter (str): Форматер, який потрібно застосувати.
        text (str, optional): Текст для форматування. За замовчуванням None.

    Повертає:
        str: Відформатований текст або порожній рядок, якщо вхідні дані некоректні.
    """
    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"**{text}**"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "header":
        level = input("Level: ")
        if not level.isdigit() or not (1 <= int(level) <= 6):
            print("The level should be within the range of 1 to 6.")
            return ""
        return f"{'#' * int(level)} {text}\n\n"
    elif formatter == "link":
        label = input("Label: ")
        url = input("URL: ")
        return f"[{label}]({url})"
    elif formatter == "inline-code":
        return f"`{text}`"
    elif formatter == "ordered-list" or formatter == "unordered-list":
        num_items = input("Number of rows: ")
        if not num_items.isdigit() or int(num_items) <= 0:
            print("The number of rows should be greater than zero.")
            return ""
        num_items = int(num_items)
        result = ""
        for i in range(1, num_items + 1):
            item = input(f"Row #{i}: ")
            if formatter == "ordered-list":
                result += f"{i}. {item}\n"
            else:
                result += f"- {item}\n"
        return result + "\n"
    elif formatter == "new-line" or formatter == "line-break":  # Add line-break here
        return "\n"
    return ""

def save_to_file(content):
    """
    Зберігає переданий текст у файл 'output.md'.

    Аргументи:
        content (str): Вміст у форматі Markdown для збереження.
    """
    with open("output.md", "w") as file:
        file.write(content)
    print("The result has been saved to output.md.")

def main():
    """Запускає головний цикл програми для введення Markdown-форматування."""
    available_formatters = {"plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
                            "unordered-list", "new-line", "line-break"}  # Include line-break here
    special_commands = {"!help", "!done"}
    markdown_text = ""

    while True:
        user_input = input("Choose a formatter: ").strip()

        if user_input in special_commands:
            if user_input == "!help":
                print_help()
            elif user_input == "!done":
                save_to_file(markdown_text)  # Save the result to the file before exiting
                break
        elif user_input in available_formatters:
            if user_input == "new-line" or user_input == "line-break":
                markdown_text += apply_format(user_input)
            elif user_input == "header":
                text = input("Text: ")
                markdown_text += apply_format(user_input, text)
            elif user_input == "link":
                markdown_text += apply_format(user_input)
            elif user_input in {"ordered-list", "unordered-list"}:
                markdown_text += apply_format(user_input)
            else:
                text = input("Text: ")
                markdown_text += apply_format(user_input, text)
            print(markdown_text)
        else:
            print("Unknown formatting type or command")

if __name__ == "__main__":
    main()
