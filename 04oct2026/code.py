security_code=float(input("Enter the security code:"))

if 1000<=security_code<=9999:
    print("code accepted")
else:
    print("code not in range")