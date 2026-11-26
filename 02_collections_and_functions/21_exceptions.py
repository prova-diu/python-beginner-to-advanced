def positive_integer(text):
    value = int(text)
    if value <= 0:
        raise ValueError("The number must be greater than zero.")
    return value


if __name__ == "__main__":
    for text in ["4", "hello", "0"]:
        try:
            number = positive_integer(text)
        except ValueError as error:
            print(f"Could not use {text!r}: {error}")
        else:
            print("Accepted:", number)
        finally:
            print("Finished this attempt.")
