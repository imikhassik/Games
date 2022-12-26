import requests
import json


class APIException(Exception):
    pass


class Conversion:
    @staticmethod
    def get_price(base, quote, amount):
        response = requests.get(f'https://api.exchangerate.host/convert?from={base}&to={quote}')
        data = json.loads(response.content)
        return data['info']['rate'] * float(amount)
