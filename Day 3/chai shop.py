from abc import ABC,abstractmethod
class Chai(ABC):
    def  __init__(self,name,base_price,quantity_in_stock):
        self.name=name
        self.base_price=base_price
        self.quantity_in_stock=quantity_in_stock
        @abstractmethod
        def calculate_price(self):
            pass
        @abstractmethod
        def display_info(self):
            pass
class Masalachai(Chai):
    def  calculate_price(self):
        revised_price = self.base_price+10
        return revised_price
    def display_info(self):
        print(f"Name:{self.name}Price per cup:{self.calculate_price()}Stock:{self.quantity_in_stock}")

class Gingerchai(Chai):
    def  calculate_price(self):
        revised_price = self.base_price+8
        return revised_price
    def display_info(self):
        print(f"Name:{self.name}Price per cup:{self.calculate_price()}Stock:{self.quantity_in_stock}")

class Elaichichai(Chai):
    def  calculate_price(self):
        revised_price = self.base_price+12
        return revised_price
    def display_info(self):
        print(f"Name:{self.name}Price per cup:{self.calculate_price()}Stock:{self.quantity_in_stock}")

class ChaiInventory:
    def __init__(self):
        self.Inventory = []

    def add_chai(self,chai_obj):
        self.Inventory.append(chai_obj)

    def show_inventory(self):
        for chai in self.Inventory:
            chai.display_info()

    def get_total_inventory_value(self):
        total = 0
        for chai in self.Inventory:
            total += chai.calculate_price() * chai.quantity_in_stock
        return total

Inventory = ChaiInventory()

chai1 = Masalachai("Masala Chai",20,50)
chai2 = Gingerchai("Ginger Chai",18,40)
chai3 = Elaichichai("Elaichi Chai",25,30)

Inventory.add_chai(chai1)
Inventory.add_chai(chai2)
Inventory.add_chai(chai3)

Inventory.show_inventory()

print("Total Inventory Value: ₹", Inventory.get_total_inventory_value())



