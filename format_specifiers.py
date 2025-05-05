#format specifiers = {value:flags} format a value based on what 
#                    flags are inserted

price1 = 3123.21345
price2 = -234.12
price3 = 23.45

print(f"price 1 is ${price1:.3f}") #take 3 value after decimal
print(f"price 2 is ${price2:10}") #make a space before value
print(f"price 2 is ${price2:010}") #add 0 before space
print(f"price 3 is ${price3:<10}") #left justify
print(f"price 3 is ${price3:>10}") #right justify
print(f"price 3 is ${price3:^10}") #center
print(f"price 1 is ${price1:,}") #add , at thousand