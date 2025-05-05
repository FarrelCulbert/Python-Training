#while loop = execute some code WHILE some condition remains true

# name = input("enter your name: ")
# age = int(input("enter your age: "))
num = int(input("enter a number 1 - 10: "))

# while name == "": #will stop when the condition FALSE
#     print("you didnt enter your name")
#     name = input("enter your name: ")
# print(f"hello {name}")

# while age < 0:
#     print("age cant be negative")
#     age = int(input("enter your age: "))
# print(f"{age} years old")

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("enter a number 1 - 10: "))
print (f"your number {num}")

