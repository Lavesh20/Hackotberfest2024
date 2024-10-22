# Mini Quiz App

def welcome_message():
    print("Welcome to the Python Mini Quiz!")
    print("Answer the following multiple-choice questions by typing the letter corresponding to the correct answer.\n")

def ask_question(question, options, correct_answer):
    print(question)
    for key, value in options.items():
        print(f"{key}: {value}")
    answer = input("\nYour answer: ").lower()
    
    if answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer was {correct_answer.upper()}: {options[correct_answer]}\n")
        return 0

def main():
    welcome_message()
    
    # List of questions, options, and correct answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": {"a": "Berlin", "b": "Madrid", "c": "Paris", "d": "Lisbon"},
            "correct_answer": "c"
        },
        {
            "question": "Who developed Python?",
            "options": {"a": "Guido van Rossum", "b": "Elon Musk", "c": "Bill Gates", "d": "Mark Zuckerberg"},
            "correct_answer": "a"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": {"a": "Earth", "b": "Jupiter", "c": "Saturn", "d": "Mars"},
            "correct_answer": "b"
        }
    ]
    
    score = 0
    total_questions = len(questions)

    # Loop through questions
    for question_data in questions:
        score += ask_question(question_data["question"], question_data["options"], question_data["correct_answer"])

    # Final score
    print(f"Quiz completed! Your final score is {score}/{total_questions}.")

if __name__ == "__main__":
    main()
