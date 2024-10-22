import json

import requests
from requests import Response

import utils.http_methods
from utils.api import GoogleMapsApi
from utils.checking import Checking

"""Создание, изменение и удаление новой локации"""


class TestCreatePlace():

    def test_create_new_place(self):
        """Тест по созданию новой локации"""
        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации и получение place_id
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)  # вызов метода проверки создания новой локации
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get,
                                   ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                    'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        Checking.check_json_search_word_in_value(result_get, 'language', 'French')
        print(result_get)

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)  # вызов метода изменения новой локации
        Checking.check_status_code(result_put, 200)
        Checking.check_json_fields(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        print(result_put)

        print("Метод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)  # вызов метода проверки локации после изменения
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')
        print(result_get)

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_location(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_fields(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')
        print(result_delete)

        print("Метод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)  # вызов метода проверки создания новой локации
        Checking.check_status_code(result_get, 404)
        Checking.check_json_fields(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")
        print(result_get)

        print("Тестирование создание, изменение и удаление новой локации прошло успешно")


    def test_query(self):
        url = "https://dog.ceo/api/breed/hound/images"
        result = utils.http_methods.HttpMethods.get(url)

        info = result.json()
        info_messages = info.get('message')
        new_list = []
        for message in info_messages:
            if "hound-english" in message:
                new_list.append(message)
        print(len(new_list))