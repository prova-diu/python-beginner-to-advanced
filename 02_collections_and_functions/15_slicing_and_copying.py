from copy import deepcopy

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[::2])
print(numbers[::-1])

alias = numbers
alias.append(60)
print("Same object:", alias is numbers, numbers)
independent = numbers.copy()
independent.append(70)
print("Original:", numbers)
print("Copy:", independent)

rows = [[1, 2], [3, 4]]
shallow = rows.copy()
deep = deepcopy(rows)
shallow[0].append(99)
print("Original changed through the shallow copy:", rows)
print("Deep copy stayed independent:", deep)
