import random
secret = random.randint(1, 10)

while (True) :
    print("===== GUESS THE NUMBER =====")

    number = int(input("Guess a number between 1-10 !! :"))

    if number < 1 or number > 10:
        print("invalid bro..., please try again and add a number from 1-10")
        continue

    if number < secret:
        print("too low!! try again..")
    elif number > secret:
        print("too high !! try again..")
    elif number == secret:
        print("=====YOUU WOOOOONN=====")
    
    answer = input("do you want to continue? (y/n): ").strip().lower()
    if answer == "n":
            print("thanks for playing, goodbyeee!!")
            break
    elif answer == "y":
            continue
    else:
         print("please enter y or n!!: ")