from bs4 import BeautifulSoup


def parse_local_file(file_path):
    try:
        # Открываем файл с явным указанием кодировки utf-8
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        movies_dict = {}

        # Находим все блоки, которые содержат информацию о фильме
        # Важно: классы могут отличаться, ищи те, что содержат 'styles_root'
        movie_items = soup.find_all('div', class_=lambda x: x and 'styles_root' in x)

        for item in movie_items:
            # Ищем название (обычно внутри span)
            name_tag = item.find('span', class_=lambda x: x and 'mainTitle' in x)
            # Ищем рейтинг
            rating_tag = item.find('span', class_=lambda x: x and 'kinopoiskValue' in x)

            if name_tag and rating_tag:
                name = name_tag.get_text(strip=True)
                rating = rating_tag.get_text(strip=True)
                movies_dict[name] = rating

        return movies_dict

    except FileNotFoundError:
        print("Файл не найден. Проверь, что он лежит в той же папке, что и скрипт.")
        return None


if __name__ == '__main__':
    # Указываем имя файла
    file_name = 'top250.html'
    result = parse_local_file(file_name)

    if result:
        print(f"Собрано фильмов: {len(result)}")
        # Выводим словарь для проверки
        for name, rating in result.items():
            print(f"{name} — {rating}")