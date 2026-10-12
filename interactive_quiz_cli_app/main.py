# Read questions, options, and correct answers from a JSON file, calculate scores, and display results.

import json
import os

FILE_NAME = "quiz.json"

def load_quiz():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

quiz = load_quiz()

def display_questions():
    score = 0
    for item in quiz:
        print(f"Q) {item['question']}")
        for index, option in enumerate(item["options"]):
            print(f"{index + 1}. {option}")
        choice = input("Enter your choice: ").title()
        if choice == item["answer"]:
            score += 1
            print("Correct answer!")
        else:
            print("Wrong answer.")
    return score

print("Welcome to the quiz - 'How much you know JUNGLES?'")
score = display_questions()
print("...........Thanks for the QUIZ...........")
print(f"You scored: {score}/10")