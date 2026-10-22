# project.py

import random
import json
import time
import os

HISTORY_FILE = "history.json"
QUESTIONS_FILE = "questions.json"


def main():
    initialize_questions()
    print("\nWelcome to IntelliQuiz! A dynamic quiz program that tracks your progress over time.\n")
    while True:
        try:
            display_menu()
            choice = input("\nEnter your choice: ").strip()
            if choice == "1":
                run_quiz()
            elif choice == "2":
                view_history()
            elif choice == "3":
                clear_history()
            elif choice == "4":
                add_custom_question()
            elif choice == "5":
                print("\nThanks for using IntelliQuiz! Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number from 1 to 5.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


def display_menu():
    print("Menu:")
    print("1. Take a quiz")
    print("2. View quiz history")
    print("3. Clear quiz history")
    print("4. Add your own quiz question")
    print("5. Exit")


def run_quiz():
    try:
        questions = get_random_questions()
        if not questions:
            print("\nNo questions available to run a quiz.\n")
            return
        score = 0
        print("\nStarting quiz...\n")
        for i, q in enumerate(questions, 1):
            print(f"Q{i}: {q['question']}")
            for j, option in enumerate(q['options'], 1):
                print(f"   {j}. {option}")

            answer = get_user_answer(len(q['options']))
            if q['options'][answer - 1] == q['answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. Correct answer: {q['answer']}\n")

        print(f"Quiz complete! Your score: {score}/{len(questions)}\n")
        save_history(score, len(questions))
    except Exception as e:
        print(f"Failed to run quiz: {e}\n")


def get_user_answer(option_count):
    while True:
        try:
            answer = int(input("Your answer: "))
            if 1 <= answer <= option_count:
                return answer
            else:
                print("Invalid choice. Please enter a valid option number.")
        except ValueError:
            print("Invalid input. Enter a number.")


def get_random_questions():
    try:
        with open(QUESTIONS_FILE, "r") as f:
            questions = json.load(f)
        return random.sample(questions, k=min(5, len(questions)))
    except FileNotFoundError:
        print("Questions file not found.")
        return []
    except json.JSONDecodeError:
        print("Error reading questions file.")
        return []
    except Exception as e:
        print(f"Unexpected error loading questions: {e}")
        return []


def initialize_questions():
    default_questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "lambda"],
            "answer": "def"
        },
        {
            "question": "What does the // operator do in Python?",
            "options": ["Exponentiation", "Modulo", "Integer division", "Float division"],
            "answer": "Integer division"
        }
    ]
    if not os.path.exists(QUESTIONS_FILE):
        with open(QUESTIONS_FILE, "w") as f:
            json.dump(default_questions, f, indent=4)


def save_history(score, total):
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "score": score,
        "total": total
    }
    try:
        history = []
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as file:
                history = json.load(file)
        history.append(entry)
        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)
    except Exception as e:
        print(f"Error saving quiz history: {e}\n")


def view_history():
    try:
        if not os.path.exists(HISTORY_FILE):
            print("\nNo quiz history found.\n")
            return
        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)
            if not history:
                print("\nNo quiz history found.\n")
                return
            print("\nYour Quiz History:")
            for entry in history:
                print(f"Date: {entry['timestamp']} | Score: {entry['score']}/{entry['total']}")
            print()
    except json.JSONDecodeError:
        print("\nError reading quiz history file.\n")
    except Exception as e:
        print(f"Error viewing history: {e}\n")


def clear_history():
    try:
        with open(HISTORY_FILE, "w") as file:
            json.dump([], file)
        print("\nQuiz history cleared.\n")
    except Exception as e:
        print(f"Error clearing history: {e}\n")


def add_custom_question():
    try:
        question = input("\nEnter your question: ").strip()
        options = []
        print("Enter 4 options:")
        for i in range(4):
            opt = input(f"Option {i+1}: ").strip()
            options.append(opt)

        answer_index = get_custom_answer_index()
        answer = options[answer_index - 1]

        new_question = {
            "question": question,
            "options": options,
            "answer": answer
        }

        with open(QUESTIONS_FILE, "r") as f:
            questions = json.load(f)
        questions.append(new_question)
        with open(QUESTIONS_FILE, "w") as f:
            json.dump(questions, f, indent=4)
        print("\nYour question has been added successfully!\n")
    except Exception as e:
        print(f"Failed to add question: {e}\n")


def get_custom_answer_index():
    while True:
        try:
            index = int(input("Which option is the correct answer? (1-4): "))
            if 1 <= index <= 4:
                return index
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Enter a number.")


if __name__ == "__main__":
    main()