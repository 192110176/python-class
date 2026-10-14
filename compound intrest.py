def compound_interest():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the annual interest rate: "))
    t = float(input("Enter the time in years: "))

    amount = p * (1 + r / 100) ** t
    ci = amount - p

    print("Compound Interest =", round(ci, 2))
    print("Total Amount =", round(amount, 2))

compound_interest()