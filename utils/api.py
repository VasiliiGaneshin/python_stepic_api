from utils.http_methods import HttpMethods

base_url = "https://rahulshettyacademy.com"  # Базовая URL
key = "?key=qaclick123"  # Параметр для всех запросов

"""Методы для тестирования Google maps API"""


class GoogleMapsApi():

    @staticmethod
    def create_new_place():
        """Метод для создания новой локации"""
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = "/maps/api/place/add/json"  # Ресурс метода POST

        post_url = base_url + post_resource + key
        print(post_url)

        result_post = HttpMethods.post(post_url, json_for_create_new_location)
        print(result_post.json())
        print(result_post.status_code)

        return result_post

    @staticmethod
    def get_new_place(place_id):
        """Метод для проверки существования локации"""
        get_resource = "/maps/api/place/get/json"  # Ресурс метода GET

        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)

        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        print(result_get.status_code)

        return result_get

    @staticmethod
    def put_new_place(place_id):
        """Метод для изменения существования локации"""
        put_resource = "/maps/api/place/update/json"  # Ресурс метода UPDATE
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        put_url = base_url + put_resource + key
        print(put_url)

        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.status_code)
        print(result_put.json())

        return result_put

    @staticmethod
    def delete_location(place_id):
        """Метод для удаления существующей локации"""
        delete_resource = "/maps/api/place/delete/json"  # Ресурс метода DELETE
        json_for_delete_location = {
            "place_id": place_id
        }

        delete_url = base_url + delete_resource + key
        print(delete_url)

        result_delete = HttpMethods.delete(delete_url, json_for_delete_location)
        print(result_delete.status_code)
        print(result_delete.json())

        return result_delete


