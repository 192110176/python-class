def calculate_bill(total):
    if total > 2000:
        discount = total * 0.10
    else:
        discount = 0

    final_bill = total - discount

    print("Original Bill: ₹", total)
    print("Discount: ₹", discount)
    print("Final Bill: ₹", final_bill)

total = float(input("Enter total bill: ₹"))
calculate_bill(total)