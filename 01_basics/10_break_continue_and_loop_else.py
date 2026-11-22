for number in range(1, 8):
    if number % 2 == 0:
        continue
    print("Odd number:", number)

names = ["Anika", "Tahsin", "Prova"]
wanted = "Prova"
for name in names:
    if name == wanted:
        print("Found:", name)
        break
else:
    print("Name not found.")
