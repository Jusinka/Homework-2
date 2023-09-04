import requests
from datetime import datetime, timedelta
import json

# Функція для перевірки валютних символів
def check_currency_symbol(currency):
    with open('symbols.json', 'r') as symbols_file:
        symbols_data = json.load(symbols_file)
        return currency in symbols_data['symbols']

# Функція для зчитування дати в правильному форматі
def read_date():
    while True:
        date_str = input("Введіть дату у форматі YYYY-MM-DD (або Enter для поточної дати): ")
        if not date_str:
            return datetime.now().strftime('%Y-%m-%d')
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            if date <= datetime.now():
                return date.strftime('%Y-%m-%d')
            else:
                print("Введена дата в майбутньому. Використована поточна дата.")
                return datetime.now().strftime('%Y-%m-%d')
        except ValueError:
            print("Некоректний формат дати. Спробуйте ще раз.")

# Головна функція
def main():
    currency_from = input("Введіть початкову валюту (default USD): ") or "USD"
    currency_to = input("Введіть цільову валюту (default UAH): ") or "UAH"

    if not (check_currency_symbol(currency_from) and check_currency_symbol(currency_to)):
        print("Некоректні символи валют. Перевірте файл symbols.json.")
        return

    amount = float(input("Введіть суму (default 100.00): ") or 100.00)
    start_date = read_date()

    save_to_file = input("Введіть ім'я файлу для збереження результату (опціонально): ")

    result_data = [['date', 'from', 'to', 'amount', 'rate', 'result']]

    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    today = datetime.now()

    while current_date <= today:
        date_str = current_date.strftime('%Y-%m-%d')
        response = requests.get('https://api.exchangerate.host/convert', params={
            'from': currency_from,
            'to': currency_to,
            'amount': amount,
            'date': date_str
        })

        data = response.json()
        rate = data['info']['rate']
        converted_amount = data['result']

        result_data.append([date_str, currency_from, currency_to, amount, rate, converted_amount])
        current_date += timedelta(days=1)

    # Збереження результату в файл (якщо задано ім'я файлу)
    if save_to_file:
        with open(save_to_file, 'w') as file:
            for row in result_data:
                file.write(','.join(map(str, row)) + '\n')

    # Виведення результату на екран
    for row in result_data:
        print(row)

if __name__ == '__main__':
    main()