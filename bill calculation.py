def calculate_bill(price, quantity):
    total = price * quantity

    if quantity > 10:
        discount = total * 0.05
    else:
        discount = 0

    return total - discount

price = float(input("Enter item price: ₹"))
quantity = int(input("Enter quantity: "))

amount = calculate_bill(price, quantity)

print("Final Amount: ₹", amount)