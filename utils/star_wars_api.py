
from utils import http_methods, checking

"""Методы для тестирования сайта Star Wars 'swapi.dev'"""

base_url = "https://swapi.dev/api/"


class StarWarsAPI():

    @staticmethod
    def get_character(number: int):
        resource = f'people/{number}'
        get_url = base_url + resource
        print(get_url)

        response = http_methods.HttpMethods.get(get_url)
        checking.Checking.check_status_code(response, 200)
        return response

