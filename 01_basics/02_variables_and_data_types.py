name = "Prova"           # str: text
age = 20                 # int: a whole number
height_in_meters = 1.60   # float: a decimal approximation
is_learning = True       # bool: True or False
favorite_language = None # None: no value has been chosen yet

print(name, age, height_in_meters, is_learning, favorite_language)
print(type(name), type(age), type(is_learning))

age = age + 1
print("Age next year:", age)

# Conversion is explicit. Text that looks like a number is still text.
price_text = "125"
price = int(price_text)
print("Two notebooks cost:", price * 2)
