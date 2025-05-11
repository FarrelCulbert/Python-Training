# nested loop =  A loop within another loop (outer, inner)
#   outer loop:
#       inner loop:

row = int(input("enter the row: "))
columns = int(input("enter the columns: "))
symbol = input("enter symbol to use: ")

for x in range(row):
    for y in range(columns):
        print(symbol, end="")
    print()