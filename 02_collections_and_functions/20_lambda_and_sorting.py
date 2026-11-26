students = [
    {"name": "Prova", "score": 88},
    {"name": "Anika", "score": 95},
    {"name": "Mina", "score": 88},
]
by_name = sorted(students, key=lambda student: student["name"])
ranked = sorted(students, key=lambda student: (-student["score"], student["name"]))
print("Alphabetical:", by_name)
print("Highest score first, then name:", ranked)

numbers = [1, 2, 3, 4]
print("Using map:", list(map(lambda number: number * 2, numbers)))
print("Using a comprehension:", [number * 2 for number in numbers])
