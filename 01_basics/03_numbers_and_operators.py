a = 17
b = 5
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)
print("Floor divide:", a // b)
print("Remainder:", a % b)
print("Power:", b ** 2)

minutes = 145
hours, remaining_minutes = divmod(minutes, 60)
print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")
print("Floor division rounds down, even for negatives:", -17 // 5)

# Floating-point numbers are approximate. Lesson 33 covers Decimal.
print("An approximation:", 0.1 + 0.2)
print("Rounded for display:", round(0.1 + 0.2, 2))
