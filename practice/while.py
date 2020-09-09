sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'aa']
sandwich = input("witch one do you order?")
while sandwich in sandwich_orders:
        sandwich_orders.remove(sandwich)
print(sandwich_orders)