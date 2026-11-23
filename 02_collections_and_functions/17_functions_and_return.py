def greet(name):
    """Build a greeting without printing it yet."""
    return f"Hello, {name}!"


def average(scores):
    """Return the mean of a non-empty collection of scores."""
    if not scores:
        raise ValueError("Please provide at least one score.")
    return sum(scores) / len(scores)


def main():
    message = greet("Prova")
    print(message)
    print("Average:", average([80, 90, 85]))


# Importing this file will define its functions without running the demo.
if __name__ == "__main__":
    main()
