import csv


class AirportNotFoundError(Exception):
    pass


class CountryNotFoundError(Exception):
    pass


class IATACodeError(Exception):
    pass


class NoOptionsFoundError(Exception):
    pass


class MultipleOptionsError(Exception):
    pass


def search_airport(data_file, **kwargs):
    # Валідація аргументів
    if sum(arg is not None for arg in kwargs.values()) != 1:
        raise MultipleOptionsError("Exactly one search parameter is required.", kwargs)

    # Відкриття CSV-файлу
    with open(data_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Пошук за кодом IATA
        iata_code = kwargs.get('iata_code')
        if iata_code:
            if not isinstance(iata_code, str) or len(iata_code) != 3 or not iata_code.isupper():
                raise IATACodeError("Invalid IATA code format.", iata_code)

            for row in reader:
                if row['iata_code'] == iata_code:
                    return row

            raise AirportNotFoundError("Airport not found", iata_code)

        # Пошук за країною
        country = kwargs.get('country')
        if country:
            results = [row for row in reader if row['iso_country'] == country]
            if not results:
                raise CountryNotFoundError("Country not found", country)
            return results

        # Пошук за іменем
        name = kwargs.get('name')
        if name:
            results = [row for row in reader if name.lower() in row['name'].lower()]
            if not results:
                raise AirportNotFoundError("Airport not found", name)
            return results

    # Якщо жоден параметр не вказано
    raise NoOptionsFoundError("No search parameter provided.", kwargs)


try:
    result = search_airport('airport-codes_csv.csv', iata_code='00A')  # Вказано невірний IATA-код
    print(result)
except (AirportNotFoundError, CountryNotFoundError, IATACodeError, NoOptionsFoundError, MultipleOptionsError) as e:
    print(e)