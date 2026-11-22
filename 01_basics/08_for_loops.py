for number in range(1, 6):
    print(number, "squared is", number ** 2)

subjects = ["Python", "Math", "English"]
for position, subject in enumerate(subjects, start=1):
    print(f"{position}. {subject}")

total = 0
for number in range(1, 11):
    total += number
print("Sum from 1 to 10:", total)

for letter in "Prova":
    print(letter, end=" ")
print()
