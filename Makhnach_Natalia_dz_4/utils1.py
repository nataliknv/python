
import requests


def currency_rates(currency_code='', url='http://www.cbr.ru/scripts/XML_daily.asp'):

    i = requests.get(url)

    currency = i.text.split(currency_code)

    if len(currency) != 1:
        val = currency[1].split('</Value>')[0].split('<Value>')[1]

        val = float(val.replace(',', '.'))

        return(val)

    return None
print('USD = ',(currency_rates('USD')), 'EUR = ',(currency_rates('EUR')))
