from math import isqrt
from learning_tools.text_tools import clean_name


def main():
    print("Clean name:", clean_name("  anika   tahsin   prova  "))
    print("Integer square root of 81:", isqrt(81))
    print("This module's name:", __name__)


if __name__ == "__main__":
    main()
