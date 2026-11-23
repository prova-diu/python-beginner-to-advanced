def greet(name, greeting="Hello", *, uppercase=False):
    message = f"{greeting}, {name}!"
    return message.upper() if uppercase else message


def add_all(*numbers):
    return sum(numbers)


def describe(**details):
    return ", ".join(f"{key}={value}" for key, value in details.items())


def add_note(note, notes=None):
    # A default [] would be shared between calls. Create a fresh list here.
    if notes is None:
        notes = []
    notes.append(note)
    return notes


if __name__ == "__main__":
    print(greet("Prova", uppercase=True))
    print(add_all(2, 4, 6))
    print(describe(name="Prova", subject="Python"))
    print(add_note("Practice functions"))
    print(add_note("Read a book"))
