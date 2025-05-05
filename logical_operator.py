#logical operator = evaluate multiple condition (or, and , not)

temp = -2
is_raining = False

# #or
# if temp > 30 or temp < 0 or is_raining:
#     print("Outdoor event is cancelled")
# else:
#     print("Outdoor event is still scheduled")

#and
if temp >= 28 and is_raining:
    print("it is wet outside")
    print("it is raining")
elif temp <=0 and is_raining:
    print("it is cold outside")
    print("it is raining")
elif temp <=0 and not is_raining:
    print("it is cold outside")
    print("it is sunny")