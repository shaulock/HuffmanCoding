from imports import text2art, tabulate, Fore, Back, Style, init, just_fix_windows_console

# Initialise colorama
init()
# Fix the console to remove previously added colorama effects
just_fix_windows_console()
# Making the background black and text bright for the rest of the runtime
print(f'{Back.BLACK}{Style.BRIGHT}')

# This function prints the welcome art at the start of the code
def print_welcome() -> None:
    s1 = text2art('Welcome to', 'tarty1')
    s2 = text2art('Huffman', 'tarty1')
    s3 = text2art('(De) Compressor', 'tarty1')
    table = [[f'{Fore.CYAN}{Back.BLACK}{Style.BRIGHT}{s1}'],[f'{Fore.RED}{s2}'],[f'{s3}']]
    print(tabulate(table,tablefmt='plain', stralign='center'))

# This function will print the error messages in red
def print_error(s: str, **kwargs) -> None:
    print(f'{Fore.RED}{Style.BRIGHT}{s}', **kwargs)

# This function will print the input prompts in white
def print_prompt(s: str, **kwargs) -> None:
    print(f'{Fore.WHITE}{Style.BRIGHT}{s}', **kwargs)

# This function will print the menu in green
def print_menu(s: str, **kwargs):
    print(f'{Fore.GREEN}{Style.BRIGHT}{s}', **kwargs)

# This function will print bye message in magenta and exit the code after resetting all styles so we dont leave any styling after exit
def print_bye():
    print(f'\n\n\n{Fore.MAGENTA}{Style.BRIGHT}Alright! Bye! Take Care!\n\n\n{Style.RESET_ALL}')
    exit(0)

# When the code is ended through keyboard interrupt this function will be called and it will print a separate message before exiting
def print_keyboard_interrupt_bye():
    print_error(f'\n\n\nRUDE!!! BYE!!!\n\n\n{Style.RESET_ALL}')
    exit(0)

# This function prints normal messages (if any) in yellow
def print_normal(s: str, **kwargs):
    print(f'{Fore.YELLOW}{Style.BRIGHT}{s}', **kwargs)