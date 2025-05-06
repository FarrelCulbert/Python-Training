hidden_num = 44
change = 0
guess = 0

while change <=6 :
    change += 1
    guess = int(input("input number 1-100: "))
    if guess < hidden_num:
        print ("larger")
    elif guess > hidden_num:
        print ("smaller")
    elif guess == hidden_num:
        print(f"Correct!! the number is {guess}, you guessed in the {change} changes")
        break
else:
    print("sorry, Your chances are up!!")
       