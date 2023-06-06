import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(
                f'Невозможно перевести одинаковые валюты "{base}"')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту "{quote}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount}"')

        api_url = 'https://min-api.cryptocompare.com/data/price?' \
                  f'fsym={quote_ticker}&tsyms={base_ticker}'
        r = requests.get(api_url)
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base
