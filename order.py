class Order:
    def __init__(self, order_id, item_id, item_name, quantity, total, status="active"):
        self.order_id = order_id
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = quantity
        self.total = total
        self.status = status

    def cancel_order(self):
        self.status = "cancelled"

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        self.total = self.calculate_total()

    def calculate_total(self):
        return self.quantity * self.price_per_item()  # Assuming price_per_item is defined elsewhere

    def price_per_item(self):
        # Placeholder for actual price retrieval logic
        return 0  # Replace with actual logic to get the price of the item

    def to_dict(self):
        return {
            "id": self.order_id,
            "item_id": self.item_id,
            "item_name": self.item_name,
            "quantity": self.quantity,
            "status": self.status,
            "total": self.total
        }