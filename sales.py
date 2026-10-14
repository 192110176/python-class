total = 0
for i in range(1, 6):
    bill = float(input("Enter customer bill: "))
    total = total + bill
average = total / 5

print("Total Sales: ₹", total)
print("Average Bill: ₹", average)