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

    if not kwargs:
        raise NoOptionsFoundError("No search parameter provided.")
    if len(kwargs) > 1:
        raise MultipleOptionsError("Only one search parameter is allowed.")


    with open(data_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)


        iata_code = kwargs.get('iata_code')
        if iata_code:
            if not isinstance(iata_code, str) or len(iata_code) != 3 or not iata_code.isupper():
                raise AirportNotFoundError("Invalid IATA code format.", iata_code)

            for row in reader:
                if row['iata_code'] == iata_code:
                    return row

            raise AirportNotFoundError("Airport not found", iata_code)


        country = kwargs.get('country')
        if country:
            results = [row for row in reader if row['iso_country'] == country]
            if not results:
                raise CountryNotFoundError("Country not found", country)
            return results


        name = kwargs.get('name')
        if name:
            results = [row for row in reader if name.lower() in row['name'].lower()]
            if not results:
                raise AirportNotFoundError("Airport not found", name)
            return results


try:
    result = search_airport('airport-codes_csv.csv', iata_code='NS')
    print(result)
except (AirportNotFoundError, CountryNotFoundError, NoOptionsFoundError, MultipleOptionsError) as e:
    print(e)

try:
    result = search_airport('airport-codes_csv.csv', iata_code='JFK', country='US')
    print(result)
except MultipleOptionsError as e:
    print(e)

try:
    result = search_airport('airport-codes_csv.csv')
    print(result)
except NoOptionsFoundError as e:
    print(e)

try:
    result = search_airport('airport-codes_csv.csv', country='XYZ')
    print(result)
except CountryNotFoundError as e:
    print(e)
