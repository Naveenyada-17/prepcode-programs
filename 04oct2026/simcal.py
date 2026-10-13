num_1=int(input("enter num1:"))
num_2=int(input("enter num2:"))
operator = input("operator:")

if operator == "+":
    print(num_1+num_2)
elif operator == "-":
    print(num_1-num_2)
elif operator == "/":
    print(num_1/num_2)
elif operator == "*":
    print(num_1*num_2)
else:
    print("invalid operation")
