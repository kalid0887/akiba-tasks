student_name = input("enter your name: ")
python_score = float(input("enter your python score: "))
english_score = float(input("enter your english score: "))
maths_score = float(input("enter your math score: "))

print("\n========================================\n")
print("\t STUDENT SCORE\t")
print("========================================\n")

print(f"student name: {student_name.title()}")

print(f"Python   :{python_score}")
print(f"English  :{english_score}")
print(f"Maths    :{maths_score}")
print("----------------------------")

print(f"Average: {round((maths_score + english_score + python_score) / 3, 2)}")
print("========================================\n")
