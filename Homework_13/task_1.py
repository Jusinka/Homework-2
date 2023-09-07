import csv


class Product:
    def __init__(self, name, product_type, price):
        if product_type not in ['coffee', 'tea', 'additional', 'bakery']:
            raise ValueError("Неприпустимий тип продукту")
        self.name = name
        self.product_type = product_type
        self.price = price

    def __str__(self):
        return f"{self.product_type.capitalize()}: {self.name}, ціна: {self.price}грн."


class Store:
    def __init__(self):
        self.inventory = {}

    def import_products(self, file_name, quantity=5):
        try:
            with open(file_name, 'r', encoding='utf8', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Назва']
                    product_type = row['Тип']
                    price = float(row['Ціна'])
                    if product_type not in self.inventory:
                        self.inventory[product_type] = []
                    for _ in range(quantity):
                        self.inventory[product_type].append(Product(name, product_type, price))
            print(f"Продукти імпортовано з файлу {file_name}")

        except FileNotFoundError:
            print(f"Файл {file_name} не знайдено.")
        except Exception as e:
            print(f"Помилка імпорту продуктів: {str(e)}")

    def get_products_by_type(self, product_type):
        if product_type == 'all':
            all_products = []
            for products in self.inventory.values():
                all_products.extend(products)
            return all_products
        elif product_type in self.inventory:
            return self.inventory[product_type]
        else:
            return []

    def get_total_price(self):
        total_price = 0
        for product_type in self.inventory:
            for product in self.inventory[product_type]:
                total_price += product.price
        return total_price

    def sell_product(self, product_name, product_type):
        if product_type in self.inventory:
            for product in self.inventory[product_type]:
                if product.name == product_name:
                    self.inventory[product_type].remove(product)
                    print(f"Продано: {str(product)}")
                    return
        print("Такого продукту не знайдено у магазині")

    def combine_products(self, product1_name, product2_name, new_product_name):
        coffee_products = self.get_products_by_type('coffee')
        additional_products = self.get_products_by_type('additional')

        product1 = None
        product2 = None

        for product in coffee_products:
            if product.name == product1_name:
                product1 = product
            if product.name == product2_name:
                product2 = product

        if product1 is None or product2 is None:
            print("Не вдалося знайти продукти для поєднання")
            return

        combined_price = product1.price + product2.price
        new_product = Product(new_product_name, 'coffee', combined_price)
        self.inventory['coffee'].append(new_product)
        print(f"Створено новий продукт: {str(new_product)}")


# Створення об'єкту магазину
my_store = Store()

# Імпорт продуктів із файлу
my_store.import_products('inventory.csv')

# Отримання списку всіх продуктів
all_products = my_store.get_products_by_type('all')
for product in all_products:
    print(product)

# Отримання загальної вартості продуктів
total_price = my_store.get_total_price()
print(f"Загальна вартість продуктів у магазині: {total_price}грн.")

# Продаж продукту
my_store.sell_product('Еспресо', 'coffee')

# Поєднання продуктів для створення Latte