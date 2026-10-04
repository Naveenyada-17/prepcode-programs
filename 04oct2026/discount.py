price=float(input("Enter the price : "))
discount=int(input("Enter discount : "))

discount_amount=(discount/100)*price

print(f"discount amount : {discount_amount}")
print(f"Total amount : {price-discount_amount}")