import os
import requests

BASE_URL_API = 'https://swapi.py4e.com/api'
SAVE_TO_DIR = 'data'


class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path=''):
        """
        Функция получает на вход ссылку, выполняет GET-запрос
        и возвращает объект класса Response
        """
        url = f'{self.base_url}{path}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as err:
            print(f'HTTP error: {err}')
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')


class SWRequester(APIRequester):
    def get_sw_categories(self):
        """
        Выполняет get-запрос к base_url.
        Если он удачный, возвращает список категорий данных.
        Если запрос упал - возвращает пустой список.
        """
        response = self.get()
        # Проверим, что get-запрос вернул объект класса response
        if isinstance(response, requests.models.Response):
            categories = response.json()
            return list(categories.keys())
        else:
            return []  # Если get-запрос "упал", то пустой список

    def get_sw_info(self, sw_type: str):
        """
        Делает GET-запрос к base_url/<sw_type>/ и возвращает ответ как строку.
        Предварительно проверяет, что sw_type — допустимая категория.
        В случае ошибки возвращает строку с описанием ошибки.
        """
        categories = self.get_sw_categories()
        if sw_type not in categories:
            return f'Ошибка: {sw_type} не является допустимой категорией из ' \
                   f'{", ".join(categories)}'
        else:
            response = self.get(f'/{sw_type}')
            return response.text


def save_sw_data():
    """
    Через API получает данные по категориям SWAPI
    Создает директорию data и сохраняет результат в формате <категория>.txt
    """
    sw = SWRequester(BASE_URL_API)
    os.makedirs(f'{SAVE_TO_DIR}', exist_ok=True)
    sw_categories = sw.get_sw_categories()
    for sw_category in sw_categories:
        sw_data = sw.get_sw_info(sw_category)
        with open(f'{SAVE_TO_DIR}/{sw_category}.txt', 'w') as f:
            f.write(sw_data)
