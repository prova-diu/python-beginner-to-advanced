raw_name = "  anika tahsin prova  "
name = raw_name.strip().title()
print(f"Hello, {name}!")
print("Original:", repr(raw_name))
print("Length:", len(name))
print("First letter:", name[0])
print("Last letter:", name[-1])
print("First five characters:", name[:5])
print("Uppercase:", name.upper())
print("Contains Tahsin:", "Tahsin" in name)

words = "Python is fun".split()
print(words)
print(" / ".join(words))
print("I like Java".replace("Java", "Python"))
price = 125.5
print(f"Price: {price:.2f}")
