def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_username(username):
    return len(username) >= 3

def format_order_display(order):
    return f"Order ID: {order['id']} | Item: {order['item_name']} | Qty: {order['quantity']} | Total: ${order['total']}"

def filter_active_orders(orders):
    return [order for order in orders if order['status'] == 'active']

def calculate_total_price(quantity, price_per_item):
    return quantity * price_per_item

def format_inventory_item(item):
    return f"{item['name']} | Stock: {item['stock']} | Price: ${item['price']}"