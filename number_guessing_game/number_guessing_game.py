# Number Guessing Game: Generates a secret number and gives hints ("Too high / Too low") until the user guesses correctly.

import random

# random.randint(a, b) returns a randomly selected integer from the inclusive range [a, b], meaning both a and b can be included
random_num = random.randint(1, 100)
# print(random_num)

def match_numbers(number):
    if number == random_num:
        return f"Well done! That's correct, {random_num} was the number."
    elif random_num > number:
        if random_num - number > 20:
            return f"Increase by 20 or more"
        elif random_num - number > 10:
            return f"Increase by 10 or more"
        else:
            return f"Very close, you have to increase by some single digit number."
    elif number > random_num:
        if number - random_num > 20:
            return f"Decrease by 20 or more"
        elif number - random_num > 10:
            return f"Decrease by 10 or more"
        else:
            return f"Very close, you have to decrease by some single digit number."

score = 0
while True:
    score += 1
    try:
        choice = int(input("Guess the number in inclusive range of 1-100: "))
    except ValueError:
        print("Please enter a value in inclusive range of 1-100 only.")
        continue
    if choice >= 1 and choice <= 100:
        match_nums = match_numbers(choice)
        print(match_nums)
        if choice == random_num:
            print(f"You took {score} tries to guess it correctly.")
            break
    else:
        print("You have to enter a value in inclusive range of 1-100 only.")
        continue