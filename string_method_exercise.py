#validate user input exercise
# 1. username no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("enter your username: ")


if len(username) <= 12 and username.isalpha() and username.find(" ")== -1:
    print ("Your username valid")
else:
    print ("Your username not valid")

#-1 is number for python didnt find the object