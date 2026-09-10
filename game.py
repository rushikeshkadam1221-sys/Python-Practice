#Guessing Game
import random

def play_game():
    lucky_num = random.randint(1, 100)
    chances = 10
    
            
    while chances > 0:
        user_num = int(input("Guess the lucky number: "))

        if user_num == lucky_num:
            print("You won. Game Over!!")
            break 
        elif user_num < lucky_num:
            print("Too low")
        else:
            print("Too High")

        chances -= 1
        print("Chances left:", chances)

    if chances == 0 and user_num != lucky_num:
        print("You lost! The lucky number was:", lucky_num)

    print("Thank you for playing")


play_game()