notebook_price = 45
pen_price = 20

notebook_quantity = int(input("Enter notebook count:"))
pen_quantity = int(input("Enter pen count:"))

notebook_total = notebook_price * notebook_quantity
pen_total = pen_price * pen_quantity

total_amont = notebook_total + pen_total

print("notebook total=", notebook_total)
print("pen total=", pen_total)
print("Total Amount=", total_amont)
