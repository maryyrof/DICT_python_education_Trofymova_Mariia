import requests
from bs4 import BeautifulSoup
import string
import os


def save_article_content(article_url, article_title, page_num):
    """
    Зберігає вміст статті у файл.
    :param article_url: URL статті
    :param article_title: Назва статті
    :param page_num: Номер сторінки для збереження в каталозі
    """
    try:
        response = requests.get(article_url, timeout=10)  # додано timeout
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            article_body = soup.find('div', class_='body')

            if article_body:
                article_text = article_body.get_text().strip().replace('\n', ' ').replace('  ', ' ')
                clean_title = article_title.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_')
                file_name = f"Page_{page_num}/{clean_title}.txt"
                os.makedirs(os.path.dirname(file_name), exist_ok=True)

                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(article_text)

                print(f"Saved article: {file_name}")
            else:
                print(f"Failed to find article body for {article_title}.")
        else:
            print(f"The article page returned {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article {article_title}: {e}")


def fetch_page_content(page_url):
    """
    Отримує HTML-контент сторінки.
    :param page_url: URL сторінки
    :return: Soup-об'єкт для обробки сторінки
    """
    try:
        response = requests.get(page_url, timeout=10)  # додано timeout
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            print(f"The URL returned {response.status_code} for {page_url}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page {page_url}: {e}")
        return None


def filter_articles_by_type(articles, article_type_filter):
    """
    Фільтрує статті за типом.
    :param articles: Список статей на сторінці
    :param article_type_filter: Тип статті для фільтрації
    :return: Список статей, що відповідають фільтру
    """
    filtered_articles = []
    for article in articles:
        article_type = article.find('span', {'data-test': 'article.type'})
        if article_type and article_type.get_text() == article_type_filter:
            filtered_articles.append(article)
    return filtered_articles


def process_articles_on_page(soup, page_num, article_type_filter):
    """
    Обробляє всі статті на сторінці.
    :param soup: Soup-об'єкт сторінки
    :param page_num: Номер сторінки
    :param article_type_filter: Тип статей для фільтрації
    """
    articles = soup.find_all('article')
    filtered_articles = filter_articles_by_type(articles, article_type_filter)

    for article in filtered_articles:
        article_link = article.find('a', {'data-track-action': 'view article'})
        if article_link:
            article_url = 'https://www.nature.com' + article_link.get('href')
            article_title = article_link.get_text().strip()
            save_article_content(article_url, article_title, page_num)


def fetch_articles(url, pages, article_type_filter):
    """
    Завантажує і зберігає статті за вказаними параметрами.
    :param url: Базова URL-адреса для статей
    :param pages: Кількість сторінок для парсингу
    :param article_type_filter: Тип статей для фільтрації
    """
    try:
        for page_num in range(1, pages + 1):
            page_url = f"{url}&page={page_num}"
            print(f"Fetching articles from {page_url}...")

            soup = fetch_page_content(page_url)

            if soup:
                os.makedirs(f"Page_{page_num}", exist_ok=True)
                process_articles_on_page(soup, page_num, article_type_filter)

                print(f"Finished processing Page {page_num}.")
            else:
                print(f"Failed to process Page {page_num}.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles list: {e}")


def main():
    """
    Основна функція для запуску парсингу статей за заданими параметрами.
    """
    pages = int(input("Input the number of pages:\n> "))
    article_type_filter = input("Input the article type (e.g., 'Nature Briefing'):\n> ")

    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2022"
    fetch_articles(url, pages, article_type_filter)

    print("Saved all articles.")


if __name__ == "__main__":
    main()
