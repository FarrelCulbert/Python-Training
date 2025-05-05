#temp converter

unit = input ("Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: ") )

if unit == "C":
    temp = (temp*9/5)+32
    unit = "F"
elif unit == "F":
    temp = (temp-32)*5/9
    unit = "C"
else:
    print(f"{unit} is wrong unit!!")

print(f"The convertion is {round(temp, 2)}°{unit}")