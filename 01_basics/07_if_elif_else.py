score = 76

if not 0 <= score <= 100:
    print("A score must be between 0 and 100.")
elif score >= 80:
    print("Excellent work.")
elif score >= 60:
    print("Good progress. Keep practicing.")
elif score >= 40:
    print("You passed. Review the difficult parts.")
else:
    print("Let us practice a little more.")

age = 20
category = "adult" if age >= 18 else "minor"
print("Category:", category)
