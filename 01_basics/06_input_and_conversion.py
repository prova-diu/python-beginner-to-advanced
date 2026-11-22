import sys

if "--interactive" in sys.argv:
    age_text = input("How old are you? ").strip()
else:
    age_text = "20"
    print("Sample input:", age_text)

try:
    age = int(age_text)
    if age < 0:
        print("Please enter a non-negative age.")
    else:
        print(f"Next year you will be {age + 1}.")
except ValueError:
    print("Please enter a whole number, such as 20.")
