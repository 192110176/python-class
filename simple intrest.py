def simple_interest():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the annual interest rate: "))
    t = float(input("Enter the time in years: "))

    si = (p * r * t) / 100
    amount = p + si

    print("Simple Interest =", si)
    print("Total Amount =", amount)

simple_interest()