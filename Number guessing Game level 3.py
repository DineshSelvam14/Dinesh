## Level 3: Give multiple Conditions¶
###1.User should enter the number between 1–100. If it's entered wrong, the program should say, "Invalid Number".
###2.If the user guessed number > secret number, then program should say, "Your number is greater than the secret number".
###3.If the user guessed number < secret number, then program should say, "Your number is lesser than the secret number".

print("welcome to the Number guessing game!!")
print("Guess the number between 1 to 100")


Secret_number = 98

for i in range(1,8):
    user_input = int(input("Give your guessed number:"))
    if user_input < 1 or user_input > 100:
        print("The given number is invalid!, Try again between 1 to 100 !! ")
    elif user_input > Secret_number:
        print("The given number is Higher!, Try again !! ")
    elif user_input < Secret_number:
        print("The given number is Lesser!, Try again !! ")
    else:
        print("Great !! you have guessed the number perfectly")
        print(f"Congrats!, you have guessed the number {Secret_number} in {i} attemps!!")
        break