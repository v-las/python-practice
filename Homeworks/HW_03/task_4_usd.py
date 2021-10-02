import requests
import json


def main():
    json_key_list = list(json_dict.keys())
    while True:
        print('You want to convert your USD. Choose the currency from the list:')
        for i in json_key_list:
            print(i[3:], sep=', ')
        your_currency = input('Enter your currency here: ').upper()
        got_rate = search_currency(your_currency, json_dict)
        if not got_rate[0]:
            print(got_rate[1])
            input('Press enter to continue')
            continue
        else:
            print('You want to convert USD into {}. Today rate - {}'.format(your_currency, got_rate[1]))
            break
    while True:
        print('How much money you need to convert?')
        your_amount = input('Enter your amount here: ')
        got_amount = check_amount(your_amount)
        if not got_amount[0]:
            print(got_amount[1])
            continue
        else:
            converted = got_rate[1] * got_amount[1]
            print(
                "You'll get {} {} for your {} USD".format(round(converted, 2), your_currency, round(got_amount[1], 2)))
            break
    input('Press enter to continue')
    print('=====')


def get_json():
    # access_key = '4505e7fd8444688bd3cca12508ba4d95'
    # url = 'http://api.currencylayer.com/live'
    # head = {'access_key': access_key,'currencies': }
    # json_request = requests.get(url, params=head)
    # request_text = json_request.text
    # request_list = json.loads(request_text)
    request_list = json.loads((requests.get('http://api.currencylayer.com/live',
                                            params={'access_key': '4505e7fd8444688bd3cca12508ba4d95'})).text)
    json_response = request_list.get('quotes')
    return json_response


def search_currency(contraction, parsed_json):
    currency_key_list = list(parsed_json.keys())
    rate_values_list = list(parsed_json.values())
    if contraction == '':
        result = 'Empty input. Please, enter currency from a list'
        return False, result
    currency = str('USD' + contraction)
    if currency not in currency_key_list:
        result = 'Invalid input. Please, enter currency from a list'
        return False, result
    else:
        result = rate_values_list[currency_key_list.index(currency)]
        return True, result


def check_amount(amount):
    if amount == '':
        result = 'Empty input. Please, enter an amount'
        return False, result
    try:
        amount = abs(float(amount))
    except ValueError:
        result = 'It\'s not a number. Please, enter an amount'
        return False, result
    if amount <= 0:
        result = 'We can\'t convert 0 USD. Please, enter an amount'
        return False, result
    else:
        return True, amount


json_dict = get_json()
while True:
    main()
json_response = {'USDRUB': 72.672604, 'USDEUR': 0.862404, 'USDCHF': 0.930533, 'USDGBP': 0.73828, 'USDCNY': 6.446704}