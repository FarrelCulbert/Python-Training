# collection = single "variable" used to store multiple values------note: ordered = berurutan
# list = [] ordered and changeable. dublicates OK
# set = {} unordered and immutable, but add/remove OK. NO duplicates
# tuple = () ordered and unchangeable. dublicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut")
# print(dir(fruits))
# print(len(fruits))
# print("apple" in fruits) #ordered

#fruits[0]="pineapple" #duplicate
# fruits.append("pineapple") #add
# fruits.remove("apple") #delete
# fruits.insert(1, "pineapple") #add at index
# fruits.sort() #alphabetical order (a,b,c,d,,,z)
# fruits.reverse() #reverse based on orer
# fruits.clear() #all gone
# print(fruits.index("apple"))
# print(fruits.count("banana"))

#set
#fruits.add("pineapple") #add
#fruits.remove("apple") #remove
#fruits.pop() #remove first element
#fruits.clear() #all gone


print(fruits)


# for x in fruits:
#     print(x)