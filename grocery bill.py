def grocery_bill():
    total = 0

    for i in range(5):
        name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))

        cost = quantity * price
        total = total + cost

    print("Total Bill: ₹", total)

grocery_bill()