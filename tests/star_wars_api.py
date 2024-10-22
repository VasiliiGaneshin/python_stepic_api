import requests

base_url = "https://swapi.dev/api/"


class TestStarWars():

    def __init__(self):
        pass

    def star_wars(self):
        resource_darth_vayder = f'people/4'
        get_url = base_url + resource_darth_vayder
        print(get_url)

        response = requests.get(get_url)
        print(response)

        assert response.status_code == 200, "ОШИБКА, Некорректный статус-код"
        print(f'УСПЕШНО, статус-код корректный: {response.status_code}')

        dart_vader_info = response.json()
        list_films_with_darth_vayder = dart_vader_info['films']

        all_characters = []  # Получение списка с персонажами из всех в которых снимался Darth Vader
        for film in list_films_with_darth_vayder:
            response = requests.get(film)
            assert response.status_code == 200, "ОШИБКА, Некорректный статус-код"
            print(f'УСПЕШНО, статус-код корректный: {response.status_code}')

            response_json = response.json()
            characters = response_json.get('characters')  # Получение всех значений параметра "characters"
            print(all_characters)
            for character in characters:
                all_characters.append(character)  # добавление значения в общий список

        all_unique_characters = list(set(all_characters))  # Получение списка уникальных персонажей

        for character in all_unique_characters:
            response = requests.get(character)
            assert response.status_code == 200, "ОШИБКА, Некорректный статус-код"
            print(f'УСПЕШНО, статус-код корректный: {response.status_code}')

            response_json = response.json()
            name = response_json.get('name')  # получение значения параметра "name"
            print(name)

            """Запись имени персонажа в файл"""
            with open('/Users/ganeshin_v/PycharmProjects/autotest_api/character_names.json', 'a') as files:
                files.writelines(name + '\n')


info = TestStarWars()
end = info.star_wars()
