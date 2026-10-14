def gst_calculation():
    price = float(input("Enter the price of the product: "))
    gst_percent = float(input("Enter the GST percentage: "))

    gst = (price * gst_percent) / 100
    total = price + gst

    print("GST Amount =", gst)
    print("Final Bill Amount =", total)

gst_calculation()