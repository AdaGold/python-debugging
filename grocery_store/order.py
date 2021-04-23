from grocery_store.product import create_product


def create_order(products, customer_name):
    return {
        "customer_name": customer_name,
        "products": products,
    }

def add_product(order, product):
    order["products"].append(product)

def calculate_total(order):
    total = 0
    for i in range(1, len(order["products"])):
        total += order["products"][i]["price"]
    
    return total





        