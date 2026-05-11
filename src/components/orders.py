from datetime import datetime
import uuid
from src.utils.file_handler import load_json_data, save_json_data
from src.models.order import Order

class OrderManager:
    def __init__(self, orders_file, inventory_file):
        self.orders_file = orders_file
        self.inventory_file = inventory_file
        self.orders = load_json_data(orders_file)
        self.inventory = load_json_data(inventory_file)

    def create_order(self, item_id, quantity):
        item = next((i for i in self.inventory if i["id"] == item_id), None)
        if item and item["stock"] >= quantity:
            total = quantity * item["price"]
            new_order = {
                "id": str(uuid.uuid4()),
                "item_id": item_id,
                "item_name": item["name"],
                "quantity": quantity,
                "status": "active",
                "total": total,
                "timestamp": str(datetime.now())
            }
            self.orders.append(new_order)
            item["stock"] -= quantity
            self._save_data()
            return new_order
        return None

    def cancel_order(self, order_id):
        order = next((o for o in self.orders if o["id"] == order_id), None)
        if order and order["status"] == "active":
            order["status"] = "cancelled"
            item = next((i for i in self.inventory if i["id"] == order["item_id"]), None)
            if item:
                item["stock"] += order["quantity"]
            self._save_data()
            return order
        return None

    def get_active_orders(self):
        return [o for o in self.orders if o["status"] == "active"]

    def _save_data(self):
        save_json_data(self.orders_file, self.orders)
        save_json_data(self.inventory_file, self.inventory)