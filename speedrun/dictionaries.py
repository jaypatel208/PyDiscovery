students = {
  "101": {"name": "Asha", "grade": "A"},
  "102": {"name": "Mit", "grade": "B"},
  "103": {"name": "Dhruvi", "grade": "A+"}
}

print("Student Ids:")
for student_id in students.keys():
    print(student_id)

print("\nStudent Grades:")
for data in students.values():
    print(f"{data['name']} -> Grade {data['grade']}")

students["104"] = {"name": "Hirva", "grade": "B+"}
print("\nAdded new student 104.")

removed = students.pop("102")
print(f"\nRemoved student: {removed['name']}")

print("\nFinal Students Data:")
for sid, info in students.items():
    print(f"{sid}: {info}")
