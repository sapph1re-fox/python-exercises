from input_exercise import guess_number

def check_input_validity(number):
    not_valid = True
    while not_valid:
        if number > 10 or number < 0:
            print("Not a valid input, please enter number from 1-10")
            not_valid = True
        else:
            not_valid = False
            return number
        number = guess_number()
            