from huffman_tree import generate_code_from_queue
from analyser import analyse_text, SEPARATORS
from imports import dumps

# This function converts binary (in string form) to decimal (only positive)
# Return type -> int
def binary_to_decimal(bin: str) -> int:
    # Take the characters from right to left
    # multiply it with 2 ^ (position of the character from right - 1) and store it in a list
    # sum all the elements of that list
    num_10 = sum([int(bin[-i])*2**(i-1) for i in range(1, len(bin) + 1)])
    # return the new number formed
    return num_10

# This function will split a string on given separators but also keep the separators in the list
# So we can separate a string based on separators and then be able to rejoin them to get the original string
# Return type -> list [ str ]
def separator_split(s: str, separators: str) -> list[str]:
    
    # The list of substrings that need to be returned
    substrings = []
    
    # The variable to keep track of what letters we have stored as a substring
    substring = ''
    
    # The variable to keep track is the substring in question currently
    # is a separator substring or normal one
    is_separator = False
    if s[0] in separators:
        is_separator = True
    
    # Looping on the string
    for i in s:
        
        # if the current substring is a normal one
        if not is_separator:
            
            # if the current character is a normal one
            if i not in separators:
                # add the character to the substring
                substring += i
            
            # if the current character is a separator
            else:
                # append the substring to the substrings list
                substrings.append(substring)
                # set the substring to the current character
                # which is a separator
                substring = i
                # set is_separator to True
                is_separator = True
        
        # if the current substring was a separator one
        else:
            
            # if the current character is a separator
            if i in separators:
                # add the character to the substring
                substring += i
            
            # if the current character is a normal one
            else:
                # append the substring to the substrings list
                substrings.append(substring)
                # set the substring to the current character
                # which is a normal one
                substring = i
                # set is_separator to False
                is_separator = False
    
    # if there is something still left in the substring (which there will be)
    # append it to the substrings list
    if substring:
        substrings.append(substring)
    
    # return the substrings list
    return substrings

# This function will create the binary string for a given text based on the huffman code given
# Return type -> str
def make_compressed_string(text: str, huffman_codes: dict[str: int], word_list: list[str]) -> str:

    # Separating 1s and 0s from other characters
    ones_and_zeros = separator_split(text, '01')
    # Converting the 1s and 0s using our code before converting anything else
    ones_and_zeros = [''.join([huffman_codes[i] 
                               if i in huffman_codes.keys() else i 
                               for i in word]) 
                      if '1' in word or '0' in word else word 
                      for word in ones_and_zeros]
    # concatenating the list to form a new text with all 1s and 0s converted
    text = ''.join(ones_and_zeros)
    # Separating words and separators
    # (which include 1 and 0 now because we dont want to convert them more than once)
    words = separator_split(text, SEPARATORS+'01')
    # Converting all the words (that are in the dictionary) using the code and leaving the rest
    words = [huffman_codes[word] 
             if word in word_list else word 
             for word in words]
    # concatenating the list to form a new text with all the words in dictionary converted
    text = ''.join(words)
    # Repeating the same process for the separate characters but this time only using
    # 1s and 0s as separators as everything other the them are already converted
    characters = separator_split(text, '10')
    characters = [''.join([huffman_codes[i] for i in word]) 
                  if not ('1' in word or '0' in word) else word 
                  for word in characters]
    # concatenating the list to form our final binary text with everything converted
    text = ''.join(characters)
    # Returning the compressed binary text
    return text

# This function will call the functions of this file and other necessary files
# To produce the final string that should be written to the output file
# Return type -> str
def create_string_to_write(text: str) -> str:
    # Getting the priority queue and word list from the text to be compressed
    queue, words = analyse_text(text)
    # Setting the type of the code, so we are able to call functions from the type class
    # with ease
    huffman_codes: dict
    # Getting our code
    huffman_codes = generate_code_from_queue(queue)
    # Getting the final binary string
    compressed_string = make_compressed_string(text, huffman_codes, words)
    # To encode it to the file while preserving space,
    # we have to convert 8 consecutive bits to a unicode-8 character
    # to do that we have to make sure the binary string is divisible by 8
    mod8 = len(compressed_string) % 8
    # if the mod 8 wasn't 0 we have to add leading 0s so we need to store that information
    # in the file itself, so we are able to remove the leading 0s later as well
    added_zeros = 0
    if mod8:
        added_zeros = 8 - mod8
    # adding the 0s if any
    compressed_string = '0'*added_zeros + compressed_string
    # getting 8 bit binaries from the text into a list
    binaries = [compressed_string[i:i+8] for i in range(0,len(compressed_string),8)]
    # converting the 8 bit binaries to decimal numbers (so python can convert it into ASCII)
    decimals = [binary_to_decimal(i) for i in binaries]
    # converting the decimals to 8 bit ASCII / unicode characters
    characters = [chr(i) for i in decimals]
    # writing the zeros added, the 8 bit unicode compressed characters and the code to the final string
    final_string = f'{added_zeros}' + ''.join(characters) + '\n' + dumps(huffman_codes)
    # returning the final formed string that is ready to write in the final file
    return final_string
