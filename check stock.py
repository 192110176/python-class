def check_stock(stock, required):
    if required <= 0:
        print("Enter a valid quantity")
    elif required <= stock:
        print("Stock available")
        print("Remaining stock:", stock - required)
    else:
        print("Insufficient stock")

stock = 50
required = int(input("Enter required quantity: "))
check_stock(stock, required)