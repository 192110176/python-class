stock = 50

print("Available Stock:", stock)

quantity = int(input("Enter required quantity: "))

if quantity <= 0:
    print("Please enter a valid quantity")
elif quantity <= stock:
    print("Medicine is available")
    stock = stock - quantity
    print("Remaining Stock:", stock)
else:
    print("Insufficient stock")