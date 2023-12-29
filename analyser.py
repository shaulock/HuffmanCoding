from queues import Priority_Queue
from nodes import StringNode
from exception_handler import CountLettersExpectedStringException, SplitExpectedStringExpection
from exception_handler import AnalyseWordsExpectedStringException, AnalyseTextExpectedStringException
from exception_handler import MakeQueueDictionaryStructureException, MakeQueueExpectedDictException
from exception_handler import RefineLettersDictionaryStructureException, RefineLettersExpectedDictException

# This is the global variable that will contain all the separators for when we extract words in a string
SEPARATORS = ' \n.,?!;:\'"\t'

# This function counts the number of occurrences of each of the letters in provided string
# and stores them in a dictionary
# Return type -> dict [ str : int ]
def count_letters(s: str) -> dict[str: int]:
    
    # If the passed string is not a string raise proper error
    if not isinstance(s, str):
        raise CountLettersExpectedStringException(f"""
Function Call : count_letters({s = })
Provided Value {s = } is not a string literal
""")

    # the dictionary that we will be returned later
    letters_dict = dict()
    
    # looping on the string
    for i in s:
        
        # Try incrementing the value of the current character in the dict
        try:
            letters_dict[i] += 1
        # If there was a key error, create a dictionary entry of the current character
        # and set it to 1
        except KeyError:
            letters_dict[i] = 1
    
    # return the dictionary
    return letters_dict

# This function splits a string with all delimiters provided
# a levelled down version of this exists built-in however, 
# as far as I could tell, you can't provide multiple delimiters to it so we made it for ourselves
# Return type -> list [ str ]
def split(s: str, delimiters: str = ' ') -> list[str]:
    
    # If the passed string is not a string raise proper error
    if not isinstance(s, str):
        raise SplitExpectedStringExpection(f"""
Function Call : split({s = }, {delimiters = })
Provided Value {s = } is not a string literal
""")
    
    # If the delimiters passed is not a string raise proper error
    if not isinstance(delimiters, str):
        raise SplitExpectedStringExpection(f"""
Function Call : split({s = }, {delimiters = })
Provided Value {delimiters = } is not a string literal
""")

    # If delimiters is empty, return a list with each character in the string separated
    if not delimiters:
        return [i for i in s]
    
    # the list of substrings to return
    substrings = []

    # the temporary string that will help in storing each word
    substring = ''

    # looping on the string
    for i in s:
        # if the character is in delemiters string
        if i in delimiters:
            # if len(substring) > 0
            if substring:
                # add substring to the list
                substrings.append(substring)
                substring = '' # reset the value of the substring
        # else add the character to the substring
        else:
            substring += i
    # if the substring is not empty after ending the loop
    # add the whole substring to the list of substrings
    if substring:
        substrings.append(substring)

    # return the list of substrings formed
    return substrings

# This function counts occurrences of words in the string provided and returns a dictionary
# Like the one with letters, except now we will be looping on each word
# Return type -> dict [ str : int ]
def analyse_words(s: str) -> dict[str: int]:
    
    # If the passed string is not a string, raise proper error
    if not isinstance(s, str):
        raise AnalyseWordsExpectedStringException(f"""
Function Call : analyse_words({s = })
Provided Value {s = } is not a string literal
""")

    # this is the dict we will return
    words_dict = dict()
    
    # first we will split the string using the split method we made, using the delimiters already created
    words = split(s, SEPARATORS)
    # count the number of each word and update the dictionary accordingly just like we did with letters
    for word in words:
        # except this time, we skip over the words that have '0' or '1' in them
        # or if the words are just 1 character long, to save hassle later
        if len(word) == 1 or '1' in word or '0' in word:
            continue
        # updating the dictionary of words
        try:
            words_dict[word] += 1
        except KeyError:
            words_dict[word] = 1

    # creating a temporary dictionary from the words_dict
    # without the words that had the value of 1
    temp_dict = {key: value for key, value in words_dict.items() if not value == 1}
    # now replacing the old dict with the new formed one
    words_dict = temp_dict
    # deleting the temporary dict to save memory
    del temp_dict
    # returning the new dict formed
    return words_dict

# This function verifies a dictionary by checking the types of it's key and value pairs
# if the passed value is not a dictionary it returns (False, )
# if the types of the dictionary's key and value dont match it returns (False, (key, value))
# if evberything checks out it returns (True, )
# Return type -> tuple
def is_valid_dict(d: dict, key_type: type = str, value_type: type = int) -> tuple:
    if not type(d) == dict:
        return (False,)
    for key, value in d.items():
        if not (type(key) == key_type and type(value) == value_type):
            return (False, (key, value))
    return (True,)

# This function converts an an obj to it's str form
# if the obj is a dictionary it will make it readable
# else it will call the str function on the obj to trigger that class's __str__() function
# Return type -> str
def str_rep(obj) -> str:
    
    # creating the str representation of the obj
    str_rep_obj = '{\n\t' + ',\n\t'.join([f'{f'\'{i}\'' 
                     if type(i)==str 
                     else i} : {f'\'{v}\'' 
                                if type(v) == str 
                                else v}' 
                  for i, v in obj.items()]) + '\n}' if type(obj) == dict else str(obj)

    # Returning the str representation
    return str_rep_obj

# This function will take the dictionary containing words and the dictionary containing letters
# It will then remove refine the letters dictionary by reducing the redundancies
# That occur when a letter in the letters dictionary is also inside a word in the words dictionary
# Return type -> dict [ str : int ]
def refine_letters(words: dict[str: int], letters: dict[str: int]) -> dict[str: int]:
    
    # creating a string representation of the arguments for easy error messages
    str_rep_letters = str_rep(letters)
    str_rep_words = str_rep(words)

    # storing the validity results from the is_valid_function
    words_validity = is_valid_dict(words)
    letters_validity = is_valid_dict(letters)
    
    # If words is not valid raise proper exception
    if not words_validity[0]:
        if len(words_validity) == 2:
            key, value = words_validity[1]
            raise RefineLettersDictionaryStructureException(f"""
Function Call : refine(words = {str_rep_words},\n letters = {str_rep_letters}).
The pair {key = }, {value = } in words does not meet the requirements (key: str, value: int).
""")
        raise RefineLettersExpectedDictException(f"""
Function Call : refine({words = }, letters = {str_rep_letters})
Provided Value {words = } is not a dictionary.
""")

    # If letters is not valid raise proper exception
    if not letters_validity[0]:
        if len(letters_validity) == 2:
            key, value = letters_validity[1]
            raise RefineLettersDictionaryStructureException(f"""
Function Call : refine(words = {str_rep_words},\n letters = {str_rep_letters}).
The pair {key = }, {value = } in letters does not meet the requirements (key: str, value: int).
""")
        raise RefineLettersExpectedDictException(f"""
Function Call : refine(words = {str_rep_words},\n {letters = })
Provided Value {letters = } is not a dictionary.
""")

    del str_rep_letters, str_rep_words, letters_validity, words_validity

    # Creating a list of keys of letters dict, so we don't call the same function everytime
    letters_keys = [i for i in letters.keys()]
    # looping on the words
    for key_2 in words.keys():
        # looping on letter in each word
        for i in key_2:
            # if the letter is found in the letters dict
            if i in letters_keys:
                # reduce the count of the letter in letters dict 
                # by the count of the word in words dict
                letters[i] -= words[key_2]
    
    # Now we need to remove the letters that have 0 count in the letters dict
    # So we dont use them later when forming our queue
    temp = {key: value for key, value in letters.items() if not value == 0}
    letters = temp
    # deleting the temporary dict to save space
    del temp
    # returning the letters dict
    return letters

# This function will take a dictionary and return a priority queue made from that string
# Return type -> PriorityQueue
def make_queue(entity_dict: dict[str: int]) -> Priority_Queue:
    
    str_rep_entity_dict = str_rep(entity_dict)
    entity_dict_validity = is_valid_dict(entity_dict)

    # If the entity_dict is not valid raise proper exception
    if not entity_dict_validity[0]:
        if len(entity_dict_validity) == 2:
            key, value = entity_dict_validity[1]
            raise MakeQueueDictionaryStructureException(f"""
Function Call : make_queue(entity_dict = {str_rep_entity_dict})
The pair {key = }, {value = } in entity_dict does not meet the requirements (key: str, value: int).
""")
        raise MakeQueueExpectedDictException(f"""
Function Call : make_queue({entity_dict = })
Provided Value {entity_dict = } is not a dictionary.
""")
    
    del entity_dict_validity, str_rep_entity_dict

    # If the dictionary does not follow the given structure
    # where key is a string and value is an integer
    # we raise proper error
    for key, value in entity_dict.items():
        if not (isinstance(key, str) and isinstance(value, int)):
            raise MakeQueueDictionaryStructureException(f"""
Function Call : make_queue(entity_dict = {str_rep(entity_dict)})
The pair {key = }, {value = } does not meet the requirements (key: str, value: int).
""")
    # Initialise an object of the priority queue class
    entity_queue = Priority_Queue()
    
    # loop over each entry in the entity dictionary
    for i in entity_dict:
        # create a string node from the item
        entity_node = StringNode(i, entity_dict[i])
        # add the item to the priority queue
        entity_queue.enqueue(entity_node)
    
    # return the priority queue created
    return entity_queue

# This function will call all the functions in this file to analyse the text passed to it
# Return type ->  PriorityQueue
def analyse_text(text: str) -> Priority_Queue:
    
    # If the text is not a string, raise proper error
    if not isinstance(text, str):
        raise AnalyseTextExpectedStringException(f"""
Function Call : analyse_text({text = })
Provided Value {text = } is not a string literal
""")
    
    # Getting the dictionary of words mapped to their respective counts
    words = analyse_words(text)
    # Getting the dictionary of letters mapped to their respective counts
    letters = count_letters(text)
    # Refining the letters dictionary to remove redundancies
    letters = refine_letters(words, letters)
    # Combining the letters and words dictionary into one
    combined = dict()
    combined.update(letters)
    combined.update(words)
    # Making the priority queue of the combined dictionary
    queue = make_queue(entity_dict=combined)
    # Now deleting the dictionaries that are not needed to save space
    del combined, letters, words
    # Returning the queue and word lsit as a tuple
    return queue