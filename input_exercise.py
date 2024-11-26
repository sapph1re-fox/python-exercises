from random import randint

<<<<<<< HEAD
name = input("What is your name?\n")

print("Hello", name + "!")

number = int(input("Select a number from 1 to 10. \n"))
choice = randint(0, 11)

print("You selected", number)
print("I selected", choice)
=======


def get_name():
    """
    Ask player for their name and return the name with greeting.
    """

    name = input("What is your name?\n")
    print("Hello", name + "!")
    return name

def guess_number():
    """
    Ask player to guess a number and generate random number by the program.
    """

    number = int(input("Select a number from 1 to 10. \n"))
    choice = randint(0, 11)
    print("You selected", number)
    print("I selected", choice)
    return number, choice
>>>>>>> 9d79ca0 (Add input exercise.)
