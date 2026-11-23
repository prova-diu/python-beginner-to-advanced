squares = [number ** 2 for number in range(1, 6)]
even_squares = [number ** 2 for number in range(1, 11) if number % 2 == 0]
labels = ["even" if number % 2 == 0 else "odd" for number in range(5)]
lengths = {word: len(word) for word in ["learn", "practice", "build"]}
initials = {name[0] for name in ["Anika", "Ayesha", "Prova"]}
print(squares)
print(even_squares)
print(labels)
print(lengths)
print(sorted(initials))

# This generator expression supplies values lazily to sum().
total = sum(number ** 2 for number in range(1, 101))
print("Sum of squares:", total)
