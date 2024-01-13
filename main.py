from printer import *
from imports import isfile
from compressor import create_string_to_write as compress
from decompressor import create_string_to_write as decompress
from exception_handler import GetIntExpectedStringException, GetIntExpectedFunctionException
from exception_handler import GetFilePathExpectedFunctionException, GetFilePathExpectedStringException

# this function will get an integer from the user, validate it by the provided validator and returns it
# Return type -> int
def get_int(prompt: str, 
            validator = lambda _: True, 
            error_message: str = 'Please follow the rules.') -> int:
    
    # If prompt is not string, raise proper error
    if not isinstance(prompt, str):
        raise GetIntExpectedStringException(f"""
Function Call : get_int({prompt = }, {validator = }, {error_message = })
Provided value {prompt = } is not a string.
""")
    
    # If error message is not string, raise proper error
    if not isinstance(error_message, str):
        raise GetIntExpectedStringException(f"""
Function Call : get_int({prompt = }, {validator = }, {error_message = })
Provided value {error_message = } is not a string.
""")
    
    # If validator is not a function, raise proper error
    if not callable(validator):
        raise GetIntExpectedFunctionException(f"""
Function Call : get_int({prompt = }, {validator = }, {error_message = })
Provided value {validator = } is not a function.
""")
    
    # Print the prompt first so we dont print it again and again
    print_prompt(prompt)
    # Infinite loop so we can take multiple inputs if user does not co-operate
    while True:
        # Take user input
        user_inp = input(f'{Fore.WHITE}> {Fore.CYAN}{Style.BRIGHT}')
        # Try to convert it to int, if it gives error, print an error message and continue the loop
        try:
            user_inp = int(user_inp)
        except ValueError:
            print_error('Please only enter an integer.')
            continue
        # check if the validator function is able to validate the input, if yes, break the loop
        if validator(user_inp):
            break
        # if not validated, print the error message and continue the loop
        else:
            print_error(error_message)
            continue
    
    # If everything was fine, return the input
    return user_inp

# This function will get the file path from user and validates it by the provided validator and returns it
# return type -> str
def get_file_path(prompt: str, 
                  validator = lambda _: isfile(_), 
                  error_message: str = 'File Does Not Exist! Try Again.') -> str:
    
    # If prompt is not string, raise proper error
    if not isinstance(prompt, str):
        raise GetFilePathExpectedStringException(f"""
Function Call : get_file_path({prompt = }, {validator = }, {error_message = })
Provided value {prompt = } is not a string.
""")

    # If error message is not string, raise proper error
    if not isinstance(error_message, str):
        raise GetFilePathExpectedStringException(f"""
Function Call : get_file_path({prompt = }, {validator = }, {error_message = })
Provided value {error_message = } is not a string.
""")

    # If validator is not a function, raise proper error
    if not callable(validator):
        raise GetFilePathExpectedFunctionException(f"""
Function Call : get_file_path({prompt = }, {validator = }, {error_message = })
Provided value {validator = } is not a function.
""")
    
    # Print the prompt first so we dont print it again and again
    print_prompt(prompt)
    # Infinite loop so we can take multiple inputs if user does not co-operate
    while True:
        # get input
        path = input(f'{Fore.WHITE}> {Fore.CYAN}{Style.BRIGHT}')
        # If the validator function returns False we continue
        if not validator(path):
            print_error(error_message)
            continue
        # if not, we break
        else:
            break
    
    # If everything was good return the path
    return path

# This is the starting menu where user will choose to compress or decompress
MENU_FOR_INPUT = """\n\n
Do you want to -
    1. Compress
    2. Decompress
"""

# This is the menu where user will choose what type of output file he will provide
MENU_FOR_OUTPUT = """
Do you want to -
    1. Over-write a file
    2. Create a new file
"""

# This is the menu where user will choose if the program should run again or end
MENU_FOR_CONTINUE = """
Do you want to use the program again?
    1. Yes
    2. No
"""

# This is the main function of the project which will be the first to run
def main():
    # print the welcome card (only once obviously)
    print_welcome()
    # While loop so we can run the code again and again
    while True:
        # Try because we want to be able to catch if the user breaks the runtime using keyboard interrupt
        try:
            # Print the starting menu
            print_menu(MENU_FOR_INPUT)
            # get the choice
            choice = get_int(
                prompt='Enter Your Choice', 
                validator=lambda _: (_ in [1, 2]), 
                error_message='Wrong Choice! Try Again.')
            
            # Based on the choice we will compress or decompress
            # 1 is for compression
            if choice == 1:
                # get the file path
                path = get_file_path(prompt='Enter the path to the file (include extensions) to compress')
                # open the file with 8-bit utf encoding
                with open(path, 'r', encoding='utf8') as og_file:
                    # read the contents
                    og_text = og_file.read()
                    # compress the contents and make the output text
                    output_text = compress(og_text)
            # 2 is decompression but we con obviously use else as we contrained the input
            else:
                # get the file path
                path = get_file_path(prompt='Enter the path to the file (include extensions) to decompress')
                # open the file with 8-bit utf encoding
                with open(path, 'r', encoding='utf8') as og_file:
                    # read the contents
                    og_text = og_file.read()
                    # decompress the contents and make the output text
                    output_text = decompress(og_text)
            
            # print the menu to choose output
            print_menu(MENU_FOR_OUTPUT)
            # get the choice using the get_int function
            choice = get_int(
                prompt='Enter Your Choice', 
                validator=lambda _: (_ in [1, 2]), 
                error_message='Wrong Choice! Try Again.')
            
            # Based on the choice we will be able to form a different checking for file path
            # 1 is for over-writing a pre-existing file
            if choice == 1:
                # Get the file path
                path = get_file_path(
                    prompt="""Enter the path to the file (include extensions) to over-write
(BEWARE!! THE FILE WILL BE OVER-WRITTEN!)""")
                
                # Open the file with 8-bit utf encoding
                with open(path, 'w', encoding='utf8') as op_file:
                    # write the output to the this new file
                    op_file.write(output_text)
            # 2 is for creating a new output file
            else:
                # Infinite loop so we can take input again and again if user doesn't co-operate
                while True:
                    # Get file path
                    path = get_file_path(
                        prompt="""Enter the path to the file (include extensions) to create
(If you are entering folders in the path, 
make sure to use your os specific slashes and make sure the folders exist)""", 
                        validator=lambda _: (not isfile(_)), 
                        error_message='File Exists! Try Again.')
                    # The user may enter a path that cannot be formed so try to open the file
                    try:
                        # open the file with 8-bit utf encoding
                        with open(path, 'w', encoding='utf8') as op_file:
                            # write the output to this new file
                            op_file.write(output_text)
                        # if the writing was done successfully break out of the loop
                        break
                    # if the file path cannot exist, print an appropriate message and continue the loop
                    except FileNotFoundError:
                        print_error('The file path was incorrect! Try Again.')
                        continue
            
            # Now we will ask user if he/she wants to continue through the code
            print_menu(MENU_FOR_CONTINUE)
            # get the choice using the get_int function
            choice = get_int(
                prompt='Enter your choice',
                validator=lambda _: (_ in [1, 2]),
                error_message='Wrong Choice! Try Again.')
            # if the user chose to not continue, we break, else we will naturally loop back
            if choice == 2:
                break
        # if the user ended the code abruptly during execution through keyboard interrupt call the keyboard interrupt printer
        except KeyboardInterrupt:
            print_keyboard_interrupt_bye()
            # and now the code will exit here
    
    # if the user broke out of the loop without running into errors or keyboard interrupt print a thank you
    print_normal('Thank you for using our program. Hope to see you again.')
    # then print bye and exit
    print_bye()

# This line here makes sure that the main program doesn't run if someone just imports it
if __name__ == '__main__':
    # calling the main function
    main()