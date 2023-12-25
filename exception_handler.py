import traceback

class HUffmanExceptions(Exception):
    
    def __init__(self, *args: object) -> None:
        print(type(self).__name__, args[0], sep=' : ', end='\n\n')
        super().__init__(*args)
    
    pass

class AnalyserExceptions(HUffmanExceptions):
    def __init__(self, *args: object) -> None:
        print('Function was part of the analyser.py file.')
        super().__init__(*args)
    pass

class CountLettersExpectedStringException(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print('Error occurred while calling the count_letters() function')
        super().__init__(*args)
    pass

class SplitExpectedStringExpection(AnalyserExceptions):
    pass