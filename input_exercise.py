from random import randint

def get_name():
    """
    Ask player for their name and return the name with greeting.
    """

    name = input("What is your name?\n")
    print("Hello", name + "!")
    return name

def guess_number():
    """
    Ask player to guess a number.
    """

    number = int(input("Select a number from 1 to 10. \n"))
    print("You selected", number)
    return number

def get_random_number(start, end):
    """
    Generate random number by the program.
    """
    choice = randint(start, end)
    print("I selected", choice)
    return choice
