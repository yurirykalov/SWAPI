import requests


BASE_URL = 'https://swapi.py4e.com/api/'

class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path=''):
        """
        Reseives link and makes GET-request
        Returns response
        """
        url = f'{self.base_url}{path}'

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as err:
            print(f'HTTP error: {err}')
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')

class SWRequester(APIRequester):
    def get_sw_categories(self):
        """
        Makes GET-request by base SWAPI url
        If request was successful - returns SWAPI categories as list
        If request failed - returns empty list
        """

        response = self.get()

        # check check that request was successful and we have response
        if isinstance(response, requests.models.Response):
            categories = response.json()
            return list(categories.keys())
        # if request failed we return empty list
        else:
            return []


if __name__ == "__main__":   
    sw = SWRequester(BASE_URL)
    print(sw.get_sw_categories())