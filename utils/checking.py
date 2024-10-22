"""Методы для проверки наших запросов"""
import json


class Checking():

    @staticmethod
    def check_status_code(response, status_code):
        """Метод для проверки статус кода"""
        assert status_code == response.status_code, f'ОШИБКА! Статус-код не совпадает = {response.status_code}'
        print(f'Успешно! Статус-код = {response.status_code}')


    @staticmethod
    def check_json_fields(result, expected_value):
        """Метод для проверки наличия полей в ответе запроса"""
        fields = json.loads(result.text)
        assert list(fields) == expected_value, "ОШИБКА, Список полей не совпадает"
        print(list(fields))
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """Метод для проверки значений у обязательных полей в ответе запроса"""
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"Значение поля: {check_info} не совпадает c ожидаемым результатом"
        print(check_info)
        print(f'Успех! Значение поля {field_name} верно')

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        """Метод для проверки значений обязательных полей в ответе запроса с помощью поиска по определенному слову"""
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info, f'ОШИБКА, слово отсутствует в поле: {field_name}'
        print(f'Успех! слово: {search_word} есть в поле: {check_info}')


