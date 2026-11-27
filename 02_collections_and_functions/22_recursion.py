def factorial(number):
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("Use a whole number.")
    if number < 0:
        raise ValueError("Factorial is not defined here for negative numbers.")
    if number <= 1:
        return 1
    return number * factorial(number - 1)


if __name__ == "__main__":
    for number in range(7):
        print(f"{number}! = {factorial(number)}")
    # Keep these examples small. math.factorial is better for real work.
