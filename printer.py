from tabulate import tabulate
from colorama import init, just_fix_windows_console, Fore, Back, Style
from art import text2art

init()
just_fix_windows_console()

def print_welcome() -> None:
    s1 = text2art('Welcome to', 'tarty1')
    s2 = text2art('Huffman', 'tarty1')
    s3 = text2art('(De) Compressor', 'tarty1')
    table = [[f'{Fore.CYAN}{Back.BLACK}{Style.BRIGHT}{s1}'],[f'{Fore.RED}{s2}'],[f'{s3}{Style.RESET_ALL}']]
    print(tabulate(table,tablefmt='plain', stralign='center'))

def print_back_black(s: str, **kwargs: dict):
    print(f'{Back.BLACK}{s}{Style.RESET_ALL}', **kwargs)

def print_error(s: str, **kwargs: dict) -> None:
    print_back_black(f'{Fore.RED}{Style.BRIGHT}{s}', **kwargs)