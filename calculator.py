#python calculor


operator = input("enter operator (+ - * /): ")
num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))


if operator == "+":
    result = num1 + num2
    print(f"The result is {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is {round(result, 2)}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is {round(result, 2)}")
elif operator == "/":
    result = num1/num2
    print(f"The result is {round(result, 2)}")
else:
    print("you type wrong operator")
