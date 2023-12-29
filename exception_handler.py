from printer import print_error, Fore
class HUffmanExceptions(Exception):
    def __init__(self, *args: object) -> None:
        print_error(f"Exception Name : {type(self).__name__} - {args[0]}", end=f'\n{Fore.CYAN}')
        super().__init__(*args)
    
class AnalyserExceptions(HUffmanExceptions):
    def __init__(self, *args: object) -> None:
        print_error('The function was part of the analyser.py file.')
        super().__init__(*args)
    
class CountLettersExpectedStringException(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling the count_letters() function.')
        super().__init__(*args)

class SplitExpectedStringExpection(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling the split() function.')
        super().__init__(*args)

class AnalyseWordsExpectedStringException(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling the analyse_words() function.')
        super().__init__(*args)

class AnalyseTextExpectedStringException(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling the analyse_text() function.')
        super().__init__(*args)

class MakeQueueExpectedDictException(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling the make_queue() function.')
        super().__init__(*args)

class MakeQueueDictionaryStructureException(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling the make_queue() function.')
        super().__init__(*args)

class RefineLettersExpectedDictException(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling the refine_letters() function.')
        super().__init__(*args)

class RefineLettersDictionaryStructureException(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling the refine_letters() function.')
        super().__init__(*args)

class CompressorExceptions(HUffmanExceptions):
    def __init__(self, *args: object) -> None:
        print_error('The Function was part of the compressor.py file.')
        super().__init__(*args)

class BinaryStringExpectedException(CompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling binary_to_decimal() function.')
        super().__init__(*args)

class IncorrectBinaryValueException(CompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling binary_to_decimal() function.')
        super().__init__(*args)

class SeparatorSplitExpectedStringExpection(CompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling separator_split() function.')
        super().__init__(*args)

class CompressorExpectedStringException(CompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling create_string_to_write() function.')
        super().__init__(*args)

class MakeCompressedStringExpectedStringException(CompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling make_compressed_string() function.')
        super().__init__(*args)

class MakeCompressedStringExpectedDictException(CompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling make_compressed_string() function.')
        super().__init__(*args)

class MakeCompressedStringCorruptedCodeException(CompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling make_compressed_string() function.')
        super().__init__(*args)

class MakeCompressedStringDictStructureException(CompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling make_compressed_string() function.')
        super().__init__(*args)