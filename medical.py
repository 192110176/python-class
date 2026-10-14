medicine = input("Enter medicine name: ")
quantity=int(input("enter quantity:"))
price=float(input("enter the price:"))

total = quantity * price

print("medical bill:")

print("medicine name:",medicine)
print("quantity :" ,quantity)
print("price per strip ",price)
print("Total Bill: ₹", total)