python_students = {"Anika", "Prova", "Rafi"}
math_students = {"Prova", "Mina"}
print("Everyone:", sorted(python_students | math_students))
print("Both classes:", sorted(python_students & math_students))
print("Only Python:", sorted(python_students - math_students))
print("Exactly one class:", sorted(python_students ^ math_students))

languages = set()  # {} would create an empty dictionary.
languages.add("Python")
languages.add("Python")
languages.add("Java")
languages.discard("C")  # No error if the value is missing.
print("Unique languages:", sorted(languages))
print("Unique score count:", len(set([80, 90, 80, 75])))
