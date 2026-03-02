from bs4 import BeautifulSoup


def parse_local_file():
    file_path = 'top250.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        movies_dict = {}

        movie_items = soup.find_all('div', class_=lambda x: x and 'styles_root' in x)

        for item in movie_items:
            name_tag = item.find('span', class_=lambda x: x and 'mainTitle' in x)
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
    result = parse_local_file()

    if result:
        print(f"Собрано фильмов: {len(result)}")
        for name, rating in result.items():
            print(f"{name} — {rating}")
