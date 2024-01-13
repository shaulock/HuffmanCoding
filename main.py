from printer import *
from imports import isfile
from compressor import create_string_to_write as compress
from decompressor import create_string_to_write as decompress

# this function will get an integer from the user, validate it by the provided validator and returns it
# Return type -> int
def get_int(prompt: str, 
            validator = lambda _: True, 
            error_message: str = 'Please follow the rules.') -> int:
    print_prompt(prompt)
    while True:
        user_inp = input(f'{Fore.WHITE}> {Fore.CYAN}{Style.BRIGHT}')
        try:
            user_inp = int(user_inp)
        except ValueError:
            print_error('Please only enter an integer.')
            continue
        if validator(user_inp):
            break
        else:
            print_error(error_message)
            continue
    return user_inp

# This function will get the file path from user and validates it by the provided validator and returns it
# return type -> str
def get_file_path(prompt: str, 
                  validator = lambda _: isfile(_), 
                  error_message: str = 'File Does Not Exist! Try Again.') -> str:
    print_prompt(prompt)
    while True:
        path = input(f'{Fore.WHITE}> {Fore.CYAN}{Style.BRIGHT}')
        # the isfile function returns True if a file exists, else it returns False, 
        # we will ask the user to try again when it returns false
        if not validator(path):
            print_error(error_message)
            continue
        else:
            break
    return path

MENU_FOR_INPUT = """\n\n
Do you want to -
    1. Compress
    2. Decompress
"""
MENU_FOR_OUTPUT = """
Do you want to -
    1. Over-write a file
    2. Create a new file
"""

def main():
    try:
        print_welcome()
        print_menu(MENU_FOR_INPUT)
        choice = get_int('Enter Your Choice', lambda x: (x in [1, 2]), 'Wrong Choice! Try Again.')
        if choice == 1:
            path = get_file_path('Enter the path to the file (include extensions) to compress')
            with open(path, 'r') as og_file:
                og_text = og_file.read()
                output_text = compress(og_text)
        else:
            path = get_file_path('Enter the path to the file (include extensions) to decompress')
            with open(path, 'r') as og_file:
                og_text = og_file.read()
                output_text = decompress(og_text)
        print_menu(MENU_FOR_OUTPUT)
        choice = get_int('Enter Your Choice', lambda x: (x in [1, 2]), 'Wrong Choice! Try Again.')
        if choice == 1:
            path = get_file_path('Enter the path to the file (include extensions) to over-write\n(BEWARE!! THE FILE WILL BE OVER-WRITTEN!)\n')
            with open(path, 'w') as op_file:
                op_file.write(output_text)
        else:
            while True:
                path = get_file_path("""
    Enter the path to the file (include extensions) to create
    (If you are entering folders in the path, make sure to use your os specific slashes and make sure the folders exist)
    """, lambda _: (not isfile(_)), 'File Exists! Try Again.')
                try:
                    with open(path, 'w') as op_file:
                        op_file.write(output_text)
                    break
                except FileNotFoundError:
                    print_error('The file path was incorrect! Try Again.')
        print_bye()
    except KeyboardInterrupt:
        print_keyboard_interrupt_bye()

if __name__ == '__main__':
    main()