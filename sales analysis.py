def sales_analysis():
    total = 0
    highest = 0

    for i in range(7):
        sales = float(input("Enter sales amount: ₹"))
        total += sales

        if sales > highest:
            highest = sales

    average = total / 7

    print("Total Sales: ₹", total)
    print("Average Bill: ₹", average)
    print("Highest Bill: ₹", highest)

sales_analysis()