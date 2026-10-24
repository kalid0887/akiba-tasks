score = 0

questions = [
    {
        "question": "Which language are we learning?",
        "options": ["A. Python", "B. Java", "C. C++", "D. PHP"],
        "answer": "A"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Boolean", "C. List", "D. Integer"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. function", "B. define", "C. fun", "D. def"],
        "answer": "D"
    },
    {
        "question": "Which data structure stores multiple items in an ordered collection?",
        "options": ["A. List", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "A"
    }
]

def display_questions(question):
    print(question["question"])
    print(question["options"])

# display_questions(questions)


def validate_answer(answer):
    if answer in ["a", "b", "c", "d"]:
        return answer
    else:
        return "please enter the correct letter!! (a-d)"

# def check_answer(index, answer):
#     for index in questions:
#         if answer == questions[index]["answer"]:
#             print("gobez lj, u got the mark!!")
#             score += 1
#         else:
#             print("nahh, try next question")


def check_answer(question, answer):
    global score

    if answer == question["answer"].lower():
        print("gobez lij, u got the mark!!")
        score += 1
    else:
        print("nahh, try next question")

if __name__ == "__main__":
    gotonext = True

    for ques in questions:
        if gotonext:
            display_questions(ques)

            while True:
                answer = input("Enter your answer (a-d): ").lower()
                validated_answer = validate_answer(answer)

                if validated_answer in ["a", "b", "c", "d"]:
                    break

                print(validated_answer)

            check_answer(ques, validated_answer)

            goto = input("Do you want to go to the next question? (y/n): ")
            gotonext = goto.lower() == "y"

    print(f"Your final score is: {score}/{len(questions)}")
