import requests


class CurrencyModel:
    CURRENCIES_API_URL = 'https://api.bluelytics.com.ar/v2/latest'

    def get_coins(self, currency):
        try:
            response = requests.get(self.CURRENCIES_API_URL)
            response.raise_for_status()
            data = response.json()

            if currency.lower() == 'dollar':
                return data['blue']['value_avg']
            elif currency.lower() == 'euro':
                return data['blue_euro']['value_avg']

        except Exception as e:
            print(f"There was an error: {e}")
            return None

    def convert(self, value_to_convert, from_currency='pesos'):
        try:
            if from_currency == 'pesos':
                result = float(value_to_convert) / float(self.get_coins('dollar'))
            else:
                result = float(value_to_convert) * float(self.get_coins('dollar'))
            return '{:,.2f}'.format(result)

        except Exception as e:
            print(f'convert_to_dollar function error : {e}')
            return None
