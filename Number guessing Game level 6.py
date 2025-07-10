
import random

print("welcome to the Number guessing game!!")
print("Guess the number between 1 to 100")


Secret_number = random.randint(1,100)

for i in range(1,8):
    try:
        user_input = int(input("Give your guessed number:"))
        if user_input < 1 or user_input > 100:
            print("The given number is invalid!, Try again between 1 to 100 !! ")
        elif user_input > Secret_number:
            print("The given number is Higher!, Try again !! ")
        elif user_input < Secret_number:
            print("The given number is Lesser!, Try again !! ")
        else:
            print("Great !! you have guessed the number perfectly")
            break
    except ValueError:
        print("you have entered invalid values, please enter numbers between 1 to 100")
    
if Secret_number == user_input :
    print(f"Congrats!, you have guessed the number {Secret_number} in {i} attemps!!")
else:
    print("you've exceeded the limit, Try again the game from first !")
    