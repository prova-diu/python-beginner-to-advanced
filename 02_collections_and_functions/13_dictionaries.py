student = {"name": "Prova", "subject": "Python", "score": 88}
print(student["name"])
print(student.get("email", "No email saved"))
student["score"] = 92
student["city"] = "Dhaka"

for key, value in student.items():
    print(f"{key}: {value}")

words = "learn practice learn build practice learn".split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Word counts:", counts)
