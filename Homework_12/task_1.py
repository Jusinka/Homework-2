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

    def add_street(self):
        new_street = Street(len(self.streets) + 1)
        self.streets.append(new_street)

    def remove_street(self, street_number):
        if 1 <= street_number <= len(self.streets):
            del self.streets[street_number - 1]
        else:
            print("Недопустимый номер улицы")

    def add_building(self, street_number):
        if 1 <= street_number <= len(self.streets):
            street = self.streets[street_number - 1]
            new_building = Building(len(street.buildings) + 1)
            street.buildings.append(new_building)
        else:
            print("Недопустимый номер улицы")

    def remove_building(self, street_number, building_number):
        if 1 <= street_number <= len(self.streets):
            street = self.streets[street_number - 1]
            if 1 <= building_number <= len(street.buildings):
                del street.buildings[building_number - 1]
            else:
                print("Недопустимый номер здания")
        else:
            print("Недопустимый номер улицы")

# Создаем город
city = City()

# Заполняем город зданиями и населением
city.populate_city()

# Выводим общее население города
print(f"Загальне населення міста: {city.total_population()}")

# Добавляем новую улицу и здание
city.add_street()
city.add_building(4)  # Добавляем здание на четвертой улице

# Удаляем улицу и здание
city.remove_street(2)  # Удаляем вторую улицу
city.remove_building(2, 2)  # Удаляем второе здание на третьей улице

# Печатаем таблицу города после изменений
city.print_city_table()