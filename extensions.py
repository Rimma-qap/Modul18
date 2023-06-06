import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIException(f'Некорректная валюта"{quote}"\n'
                               'Список всех доступных валют - /values')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount}"')

        if quote.lower() == base.lower():
            raise APIException(
                f'Невозможно перевести одинаковые валюты "{base}"')

        api_url = 'https://min-api.cryptocompare.com/data/price?' \
                  f'fsym={quote_ticker}&tsyms={base_ticker}'
        r = requests.get(api_url)
        total_base = json.loads(r.content)[keys[base.lower()]] * amount

        return total_base
