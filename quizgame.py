# Define the quiz questions, options, and correct answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin"],
        "correct_answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Jupiter", "C. Venus"],
        "correct_answer": "A"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. CO2", "C. NaCl"],
        "correct_answer": "A"
    }
]

# Function to display the quiz questions and options
def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

# Function to check if the answer is correct and update the score
def check_answer(question, user_answer, score):
    if user_answer.upper() == question["correct_answer"]:
        print("Correct!")
        return score + 1
    else:
        print("Incorrect! The correct answer is:", question["correct_answer"])
        return score

# Function to conduct the quiz
def conduct_quiz(questions):
    score = 0
    for question in questions:
        display_question(question)
        user_answer = input("Enter your answer (A/B/C): ")
        score = check_answer(question, user_answer, score)
        print()  # Add a newline for better readability
    return score

# Function to edit the quiz questions
def edit_questions():
    print("Current quiz questions:")
    for i, question in enumerate(quiz_questions, start=1):
        print(f"{i}. {question['question']}")

    try:
        question_index = int(input("Enter the index of the question you want to edit: ")) - 1
        if question_index < 0 or question_index >= len(quiz_questions):
            print("Invalid question index!")
            return

        new_question = input("Enter the new question: ")
        new_options = [input("Enter option A: "),
                       input("Enter option B: "),
                       input("Enter option C: ")]
        new_correct_answer = input("Enter the correct answer (A/B/C): ").upper()

        quiz_questions[question_index]["question"] = new_question
        quiz_questions[question_index]["options"] = new_options
        quiz_questions[question_index]["correct_answer"] = new_correct_answer

        print("Question updated successfully!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Main function to run the quiz
def main():
    print("Welcome to the Quiz Game!")
    print("1. Start the game")
    print("2. Edit questions")
    print("3. Exit the game")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("Please answer the following questions:")
        print("--------------------------------------")
        final_score = conduct_quiz(quiz_questions)
        print("--------------------------------------")
        print("Quiz completed! Your final score is:", final_score)
    elif choice == "2":
        edit_questions()
    elif choice == "3":
        print("Exiting the game. Goodbye!")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
