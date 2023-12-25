from queues import Priority_Queue
from nodes import StringNode
from exception_handler import CountLettersExpectedStringException

# This is the global variable that will contain all the separators for when we extract words in a string
SEPARATORS = ' \n.,?!;:\'"\t'



# This function counts the number of occurrences of each of the letters in provided string
# and stores them in a dictionary
# Return type -> dict [ str : int ]
def count_letters(s: str) -> dict[str: int]:
    
    if not isinstance(s, str):
        raise CountLettersExpectedStringException(f'Function Call : count_letters({s})\nProvided Value {s} is not a string literal')

    # the dictionary that we will be returned later
    letters_dict = dict()
    
    # looping on the string
    for i in s:
        # check if the character already exists in the dictionary, 
        # if yes, increase it's count by 1
        # else set it's count to 1
        if i in letters_dict.keys():
            letters_dict[i] += 1
        else:
            letters_dict[i] = 1
    
    # return the dictionary
    return letters_dict

# This function splits a string with all delimiters provided
# a levelled down version of this exists built-in however, 
# as far as I could tell, you can't provide multiple delimiters to it so we made it for ourselves
# Return type -> list [ str ]
def split(s: str, delimiters: str = ' ') -> list[str]:
    

    
    if not delimiters:
        return list(s)
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
    
    # this is the dict we will return
    words_dict = dict()
    
    # first we will split the string using the split method we made, using the delimiters already created
    words = split(s, SEPARATORS)
    # count the number of each word and update the dictionary accordingly just like we did with letters
    for word in words:
        # except this time, we skip over the words that have '0' or '1' in them, to save hassle later
        if len(word) == 1 or '1' in word or '0' in word:
            continue
        # updating the dictionary of words
        if word in words_dict.keys():
            words_dict[word] += 1
        else:
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

# This function will take the dictionary containing words and the dictionary containing letters
# It will then remove refine the letters dictionary by reducing the redundancies
# That occur when a letter in the letters dictionary is also inside a word in the words dictionary
# Return type -> dict [ str : int ]
def refine(words: dict[str: int], letters: dict[str: int]) -> dict[str: int]:
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
# Return type -> tuple [ PriorityQueue , list [ str ] ]
def analyse_text(text: str) -> tuple[Priority_Queue, list[str]]:
    # Getting the dictionary of words mapped to their respective counts
    words = analyse_words(text)
    # Getting the dictionary of letters mapped to their respective counts
    letters = count_letters(text)
    # Refining the letters dictionary to remove redundancies
    letters = refine(words, letters)
    # Combining the letters and words dictionary into one
    combined = dict()
    combined.update(letters)
    combined.update(words)
    # Creating the list of keys in the words dictionary
    words = [i for i in words.keys()]
    # Making the priority queue of the combined dictionary
    queue = make_queue(entity_dict=combined)
    # Now deleting the dictionaries that are not needed to save space
    del combined, letters
    # Returning the queue and word lsit as a tuple
    return queue, words