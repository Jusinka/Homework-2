import random

class Building:
    def __init__(self, number):
        self.number = number
        self.population = random.randint(1, 100)

class Street:
    def __init__(self, number):
        self.number = number
        self.buildings = [Building(i) for i in range(1, random.randint(5, 21))]

class City:
    def __init__(self):
        self.streets = [Street(i) for i in range(1, random.randint(3, 11))]

    def populate_city(self):
        for street in self.streets:
            for building in street.buildings:
                print(f"Вулиця {street.number} Будинок {building.number} Населення {building.population}")

    def total_population(self):
        total_pop = 0
        for street in self.streets:
            for building in street.buildings:
                total_pop += building.population
        return total_pop

    def print_city_table(self):
        print("Вулиця   Будинок   Населення")
        for street in self.streets:
            for building in street.buildings:
                print(f"   {street.number}        {building.number}         {building.population}")

# Створюємо місто
city = City()

# Заповнюємо місто будинками та населенням
city.populate_city()

# Виводимо загальне населення міста
print(f"Загальне населення міста: {city.total_population()}")

# Друкуємо таблицю міста
city.print_city_table()