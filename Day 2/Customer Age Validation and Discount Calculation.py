customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

def is_eligible(customer):
    return 18 <= customer["age"] <= 40

def apply_discount(customer):
    discount = 0.1 if 18 <= customer["age"] <= 25 else 0.05
    customer["total_purchase"] *= (1 - discount)
    return customer

eligible_customers = list(map(apply_discount, filter(is_eligible, customers)))
print(eligible_customers)