students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]


def validate_users(grade):
    if isinstance(grade, bool) or not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
        return False
    return True


def calculateGrade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"


def calculate_average(students):
    total = 0

    if len(students) == 0:
        return 0

    for student in students:
        total += student["score"]

    average = total / len(students)
    return average


def highestAndLowest(students):
    if len(students) == 0:
        return None, None

    lowest = students[0]["score"]
    highest = students[0]["score"]

    for student in students:
        score = student["score"]

        if score < lowest:
            lowest = score

        if score > highest:
            highest = score

    return highest, lowest


def count_passed_failed(students):
    passed = 0
    failed = 0

    for student in students:
        if student["score"] >= 50:
            passed += 1
        else:
            failed += 1

    return passed, failed


def above_average_students(students):
    average = calculate_average(students)
    result = []

    for student in students:
        if student["score"] > average:
            result.append(student)

    return result


def generate_report(students):
    valid_students = []

    for student in students:
        if validate_users(student["score"]):
            valid_students.append(student)
        else:
            print("Invalid score for:", student["name"])

    if len(valid_students) == 0:
        print("No valid student records.")
        return

    average = calculate_average(valid_students)
    highest, lowest = highestAndLowest(valid_students)
    passed, failed = count_passed_failed(valid_students)
    above_average = above_average_students(valid_students)

    print("\n===== STUDENT PERFORMANCE REPORT =====")

    for student in valid_students:
        print(
            student["name"],
            "| Score:", student["score"],
            "| Grade:", calculateGrade(student["score"])
        )

    print("\nClass average:", average)
    print("Highest score:", highest)
    print("Lowest score:", lowest)
    print("Passed students:", passed)
    print("Failed students:", failed)

    print("\nStudents above class average:")

    for student in above_average:
        print(student["name"], "-", student["score"])


generate_report(students)