#Number guessing Game level 1
## Level 1. Print if the user guessed number is right or not
Secret_number = 56

User_input = int(input("Enter your guess:"))

if Secret_number == User_input:
    print("Great you guessed right!!")
else:
    print("Oops, you guessed wrong")

## Level 2. Print if the user guessed number is right or not with maximum of 7 try
    #### 2.1. For loop using to guess the number
Secret_number = 56

for i in range(0,7):   
    User_input = int(input("Enter your guess:"))
    
    if Secret_number == User_input:
        print("Great you guessed right!!")
        break
    else:
        print("Oops, you guessed wrong")


    #### 2.2. while loop using to guess the number

Secret_number = 56

while True:  
    User_input = int(input("Enter your guess:"))
    
    if Secret_number == User_input:
        print("Great you guessed right!!")
        break
    else:
        print("Oops, you guessed wrong")