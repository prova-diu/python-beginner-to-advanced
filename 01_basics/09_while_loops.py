countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Go!")

balance = 0
weeks = 0
target = 250
while balance < target:
    balance += 50
    weeks += 1
    print(f"Week {weeks}: saved {balance}")
print(f"Reached the target after {weeks} weeks.")
