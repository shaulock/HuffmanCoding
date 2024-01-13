from tabulate import tabulate
from colorama import init, just_fix_windows_console, Fore, Back, Style
from art import text2art

init()
just_fix_windows_console()
print(f'{Back.BLACK}{Style.BRIGHT}')


def print_welcome() -> None:
    s1 = text2art('Welcome to', 'tarty1')
    s2 = text2art('Huffman', 'tarty1')
    s3 = text2art('(De) Compressor', 'tarty1')
    table = [[f'{Fore.CYAN}{Back.BLACK}{Style.BRIGHT}{s1}'],[f'{Fore.RED}{s2}'],[f'{s3}']]
    print(tabulate(table,tablefmt='plain', stralign='center'))

def print_error(s: str, **kwargs) -> None:
    print(f'{Fore.RED}{Style.BRIGHT}{s}', **kwargs)

def print_prompt(s: str, **kwargs) -> None:
    print(f'{Fore.WHITE}{Style.BRIGHT}{s}', **kwargs)

def print_menu(s: str, **kwargs):
    print(f'{Fore.GREEN}{Style.BRIGHT}{s}', **kwargs)

def print_bye():
    print(f'\n\n\n{Fore.MAGENTA}{Style.BRIGHT}Alright! Bye! Take Care!\n\n\n{Style.RESET_ALL}')
    exit(0)

def print_keyboard_interrupt_bye():
    print_error(f'\n\n\nRUDE!!! BYE!!!\n\n\n{Style.RESET_ALL}')
    exit(0)

def print_normal(s: str, **kwargs):
    print(f'{Fore.YELLOW}{Style.BRIGHT}{s}', **kwargs)