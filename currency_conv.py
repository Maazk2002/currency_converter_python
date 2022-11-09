from requests import get
from pprint import PrettyPrinter                   

BASE_URL = "https://free.currconv.com/"     #url for sending our request to 
API_KEY = "382964f5be363d415c12"        

printer = PrettyPrinter()      #allows to get nicely formated output for json

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"   #link to send req for 
    url = BASE_URL + endpoint                          #currency data  
    data = get(url).json()['results']
    
    data = list(data.items())
    
    data.sort()
    
    return data 


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint              #link to send req on for exchange                                             
    data = get(url).json()                 #rate data

    if len(data) == 0:
        print('Invalid currencies.')
        return

    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()

    print("-->Welcome to the currency converter!<--")
    print("*****************************************")
    print()
    print("type 'l' for lists of the different currencies")
    print("type 'c' for convert from one currency to another")
    print("type 'r' to get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "l":
            print_currencies(currencies)
        elif command == "c":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "r":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")

main()
















