import sys


def check_parity():
    while True:
        input_value = input('Choose a number: ')
        try:
            number = float(input_value)  # why do I need to convert to float first?
            if number.is_integer():
                number = int(number)
            else:
                raise ValueError  # does this go to the next ValueError?
            if number % 2 == 0:
                return f'{number} is even'
            else:  # is 'else' necessary for readability?
                return f'{number} is odd'
        except ValueError:
            if input_value.strip() == '':  # Changed ' ' to strip() for blank space check? is it the same?
                return 'Value cannot be a blank space'
            else:
                return f'\'{input_value}\' is not an integer'


def new_number():
    while True:
        # Prompt for a new number
        print(check_parity())

        # Ask if the user wants to try a different number
        while True:
            new_input = input('Would you like to try a different number? (yes/no): ')
            if new_input.lower() in ('yes', 'y'):
                break  # where does this goes? to new_number?
            elif new_input.lower() in ('no', 'n'):
                sys.exit()  # Exit the program
            else:
                print(f'\'{new_input}\' is not a valid answer. Please type "yes" or "no".')


# Start the process, I don't get in which order are things processed
new_number()
