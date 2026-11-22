student = ("Prova", 20, "Python")
name, age, subject = student
print(f"{name} is {age} and studies {subject}.")

coordinates = (23.81, 90.41)
latitude, longitude = coordinates
print("Coordinates:", latitude, longitude)

single_item = ("Python",)  # The comma makes this a tuple.
print(type(single_item))
first, *middle, last = (1, 2, 3, 4, 5)
print(first, middle, last)
left, right = "A", "B"
left, right = right, left
print("Swapped:", left, right)

# A tuple can contain mutable objects; those objects can still change.
group = ("friends", ["Anika"])
group[1].append("Prova")
print(group)
