from pathlib import Path
import json
from models.inventory_item import InventoryItem
from utils.file_handler import load_json_data, save_json_data

class InventoryManager:
    def __init__(self, inventory_file):
        self.inventory_file = Path(inventory_file)
        self.inventory = self.load_inventory()

    def load_inventory(self):
        return load_json_data(self.inventory_file)

    def save_inventory(self):
        save_json_data(self.inventory_file, self.inventory)

    def display_inventory(self):
        if not self.inventory:
            return "No items in inventory."
        return [f"{item['name']} | Stock: {item['stock']} | Price: ${item['price']}" for item in self.inventory]

    def add_item(self, name, stock, price):
        new_item = InventoryItem(name=name, stock=stock, price=price)
        self.inventory.append(new_item.to_dict())
        self.save_inventory()

    def update_item_stock(self, item_id, quantity):
        for item in self.inventory:
            if item['id'] == item_id:
                item['stock'] += quantity
                self.save_inventory()
                return f"Updated stock for {item['name']} to {item['stock']}."
        return "Item not found."

    def get_item(self, item_id):
        for item in self.inventory:
            if item['id'] == item_id:
                return item
        return None

    def remove_item(self, item_id):
        self.inventory = [item for item in self.inventory if item['id'] != item_id]
        self.save_inventory()