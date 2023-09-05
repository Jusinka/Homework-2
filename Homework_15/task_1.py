import csv


class AirportNotFoundError(Exception):
    pass


class CountryNotFoundError(Exception):
    pass


class NoOptionsFoundError(Exception):
    pass


class MultipleOptionsError(Exception):
    pass


def search_airport(data_file, **kwargs):
    # Валідація аргументів
    if not kwargs:
        raise NoOptionsFoundError("No search parameter provided.")
    if len(kwargs) > 1:
        raise MultipleOptionsError("Only one search parameter is allowed.")

    # Відкриття CSV-файлу з кодуванням UTF-8
    with open(data_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Пошук за кодом IATA
        iata_code = kwargs.get('iata_code')
        if iata_code:
            if not isinstance(iata_code, str) or len(iata_code) != 3 or not iata_code.isupper():
                raise AirportNotFoundError("Invalid IATA code format.", iata_code)

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


try:
    result = search_airport('airport-codes_csv.csv', iata_code='NIS')
    print(result)
except (AirportNotFoundError, CountryNotFoundError, NoOptionsFoundError, MultipleOptionsError) as e:
    print(e)