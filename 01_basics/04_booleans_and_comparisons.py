score = 82
attendance = 90
print("Passed:", score >= 40)
print("Exactly eighty:", score == 80)
print("Not zero:", score != 0)
print("Eligible:", score >= 80 and attendance >= 75)
print("Needs help:", score < 40 or attendance < 60)
print("Has not passed:", not (score >= 40))
print("Valid score:", 0 <= score <= 100)

# Empty strings and collections are false in a condition.
nickname = ""
print("Has a nickname:", bool(nickname))
result = None
print("Result is missing:", result is None)  # Use 'is' for None.
