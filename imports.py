# This file will handle all imports
from os.path import isfile
from json import dumps, loads
from json.decoder import JSONDecodeError
from tabulate import tabulate
from colorama import init, just_fix_windows_console, Fore, Back, Style
from art import text2art