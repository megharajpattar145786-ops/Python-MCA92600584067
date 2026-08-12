student = {
    "name": "Varun",
    "marks": 90
}

print(student)

student["age"] = 20
student["marks"] = 90

print("Keys:", student.keys())
print("Values:", student.values())

for key, values in student.items():
    print(key, ":", values)
