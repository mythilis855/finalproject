class InventoryItem:
    def __init__(self, item_id, name, price, stock):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            raise ValueError("Insufficient stock available.")

    def to_dict(self):
        return {
            "id": self.item_id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }