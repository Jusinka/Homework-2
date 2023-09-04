import csv
from tabulate import tabulate

class Item:

    ITEM_TYPES = ['coffee', 'tea']
    LATTE_INGREDIENTS = ['Milk', 'Espresso']

    @staticmethod
    def _validate(item_type):
        if item_type not in Item.ITEM_TYPES:
            return False
        return True

    def __init__(self, name: str, price: int, item_type: str):
        self.name = name
        self.price = price
        if self._validate(item_type):
            self.item_type = item_type
        else:
            self.item_type = 'additional'

    def __str__(self):
        return f"{self.item_type}: {self.name}, price: {self.price};"

    def __repr__(self):
        return f"Type: {self.item_type}; Name: {self.name}; Price: {self.price}"

    def __add__(self, other):
        if self.name and other.name in Item.LATTE_INGREDIENTS:
            name = 'Latte'
            price = self.price + other.price
            item_type = "coffee"
            return Item(name, price, item_type)
        raise ArithmeticError(f"You can't create a Latte from {self.name} and {other.name}")


class Shop:

    def __init__(self, name="Coffee & Tea"):
        self.name = name
        self.items = []

    def __str__(self):
        return f"{self.name} shop"

    def import_inventory(self, path_to_file: str):
        with open(f"{path_to_file}", 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                name = row[0]
                item_type = row[1]
                price = int(row[2])
                quantity = 5
                if row[3]:
                    quantity = int(row[3])
                item = Item(name, price, item_type)
                self.items.append((item, quantity))

    def get_items(self, item_type: str = 'all') -> str:
        item_list = []
        headers = ["Name", "Type", "Price", "Quantity"]
        for item, quantity in self.items:
            if item_type == 'all':
                item_list.append([item.name, item.item_type, item.price, quantity])
            elif item.item_type == item_type:
                item_list.append([item.name, item.item_type, item.price, quantity])
        return tabulate(item_list, headers=headers)

    def get_total_cost(self) -> str:
        cost = 0
        for item, quantity in self.items:
            cost += item.price * quantity
        return f"Total price of all items is: {cost} UAH"

    def sell_item(self, name):
        for item in self.items:
            if item[0].name == name:
                self.items.pop(self.items.index(item))
                return print(f"{name} has been sold")


if __name__ == '__main__':
    shop = Shop()
    shop.import_inventory('inventory.csv')
    print(shop.get_total_cost())
    shop.sell_item('Green Tea')
    print(shop.get_total_cost())
    milk = Item('Milk', 10, 'additional')
    espresso = Item('Espresso', 25, item_type='coffee')
    latte = espresso + milk
    latte2 = milk + espresso
    print(latte)
    print(latte2)
    print(shop.get_items('additional'))