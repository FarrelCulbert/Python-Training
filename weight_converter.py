#python weight converter

weight = float(input("Input your weight: "))
unit = input("Kilogram or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
else:
    print(f"{unit} is wrong unit!")

print(f"The weight is {round(weight, 2)} {unit}")