def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply


def make_counter():
    count = 0

    def next_count():
        nonlocal count  # Reassign the variable from the enclosing scope.
        count += 1
        return count

    return next_count


if __name__ == "__main__":
    double = make_multiplier(2)
    print("Double 7:", double(7))
    counter = make_counter()
    print(counter(), counter(), counter())
    another_counter = make_counter()
    print("A separate counter:", another_counter())
