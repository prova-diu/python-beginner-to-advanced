def is_palindrome(text):
    cleaned = "".join(character.casefold() for character in text if character.isalnum())
    return cleaned == cleaned[::-1]


def unique_in_order(items):
    result = []
    seen = set()
    for item in items:  # This version expects hashable items.
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def fizzbuzz(limit):
    answers = []
    for number in range(1, limit + 1):
        label = ("Fizz" if number % 3 == 0 else "") + ("Buzz" if number % 5 == 0 else "")
        answers.append(label or str(number))
    return answers


if __name__ == "__main__":
    print("Palindrome:", is_palindrome("Never odd or even"))
    print("Unique:", unique_in_order([3, 1, 3, 2, 1]))
    print("FizzBuzz:", ", ".join(fizzbuzz(15)))
