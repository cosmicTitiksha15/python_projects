# This is a number guessing game where you will be also recieve comments based on number of tries you took to guess it right.
# `random` module, `while` loops, conditional logic.
import random

def guess_your_num(guessed_num):
    if random_num > guessed_num:
        if random_num - guessed_num >= 50 :
            print('Ok..you are lagging by nearly fifty.')
        elif random_num - guessed_num >= 20 :
            print("You are nearly 10 or 20 behind.")
        elif random_num - guessed_num >= 5:
            print("Ok-Ok super close. Higher!")
        else:
            print("Very close(1-5), add someting in 1 to 5 range.")
        return False
    elif random_num == guessed_num:
        print("Walllaah!, you guessed it right.")
        return True
        
    else:
        if guessed_num - random_num >= 50 :
            print('Ok..you are leading by nearly fifty.')
        elif guessed_num - random_num >= 20 :
            print("You are nearly 10 or 20 ahead.")
        elif guessed_num - random_num >= 5:
            print("Ok-Ok super close. lower!")
        else:
            print("Very close(1-5), subtract someting in 1 to 5 range.")
        return False

random_num = random.randint(1,100)
score = 0

while True:
    try:
        guessed_num = int(input("Ok..So, it's an integer in inclusive range of 1-100, make a guess : "))
        score += 1
        is_correct = guess_your_num(guessed_num)
        if is_correct:
            print(f"You guessed it right in {score} trials.")
            query = input("Wanna play again? (y/n) :")
            if query.lower() == 'y':
                random_num = random.randint(1, 100)
                score = 0
                continue
            elif query.lower() == 'n':
                print("Ok bye. See you again")
                break
            else:
                print("Uh-Oh, ok..sending you out, looks like you are done already.")
                break
    except:
        print("Please enter a valid number.")