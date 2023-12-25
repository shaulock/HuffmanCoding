from compressor import create_string_to_write as cstw
from huffman_tree import generate_tree_from_code
from nodes import LeafNode, TreeNode
from imports import loads

# This function will convert a decimal number to binary (only positive numbers)
# Return type -> str
def decimal_to_binary(deci: int) -> str:
    # Base case for recursion
    # if the number is 0, return '0'
    if deci == 0:
        return '0'
    # if the number is 1, return '1'
    if deci == 1:
        return '1'
    # if base cases not met, call the function again 
    # by passing the quotient of integer division of present integer by 2
    # and append it to the right of the mod 2 of the present integer
    return decimal_to_binary(deci//2) + f'{deci%2}'

# This function will convert a decimal number to 8 bit binary
# Return type -> str
def decimal_to_binary_8_bit(deci: int) -> str:
    # get the converted the binary string of the number
    binary = decimal_to_binary(deci)
    # get the amount of 0s to be appended at the start
    mod8 = len(binary)%8
    if mod8:
        return '0'*(8-mod8) + binary # returnign the string with added 0s
    return binary # if mod 8 was 0 we just return the string as it is

# This function will separate huffman codes and the compressed string from text provided
# Return type -> tuple [ dict [ str : int ] , str ]
def separate_huffman_codes_and_text(text: str) -> tuple[dict[str: int], str]:
    
    # creating an empty string and dictionary
    compressed_text = ''
    huffman_codes = dict()
    
    # searching the string from behind and capturing exactly where the codes start
    for i in range(len(text)-1, -1, -1):
        if text[i]=='\n':
            if text[i+1] == '{':
                # convert the codes back from string to dict
                huffman_codes = loads(text[i+1:])
                # add the rest of the string as the compressed string
                compressed_text = text[:i]
                break

    # Returning a tuple of the codes and compressed text
    return huffman_codes, compressed_text

# This function will remove added zeros during compression and
# convert the text from 8 bit unicode to 8 bit binary
# Return type -> str
def refine_text(compressed_text_from_file: str, added_zeros: int) -> str:
    # creating an empty string
    refined_text = ''
    # looping over the text
    for i in compressed_text_from_file:
        # convert the unicode character to decimal and the decimal to binary string
        refined_text += decimal_to_binary_8_bit(ord(i))
    # Removing the added zeros
    refined_text = refined_text[added_zeros:]
    # Returning our refined string
    return refined_text

# This function will decompress the refined text based on the codes provided
# Return type -> str
def decompress_text(text: str, code: dict) -> str:
    # Setting the type of the codes to be used (so it will be easy to call functions on it)
    huffman_tree: TreeNode
    # Getting the huffman Tree from the codes given
    huffman_tree = generate_tree_from_code(code)
    # Creating an empty string to store the decompressed
    decompressed_text = ''
    # setting the pointer for traversing through the tree
    pointer = huffman_tree
    # Looping over the binary string
    for i in text:
        # if the current string leads to a leafNode
        if pointer.children[int(i)].type == LeafNode:
            # add the value of the leaf node to the decompressed text list
            decompressed_text += pointer.children[int(i)].value
            # set the pointer back to the top
            pointer = huffman_tree
        # if not
        else:
            # traverse to the intended child of the pointer
            pointer = pointer.children[int(i)]
    
    # Return the decompressed text
    return decompressed_text

# This function will call all the necessary functions 
# and create the final string to be written in the output file
# Return type -> str
def create_string_to_write(text: str) -> str:
    # Separating and storing the code and compressed text
    huffman_code, compressed_text = separate_huffman_codes_and_text(text)
    # Retrieving the number of zeros that were added during compression
    added_zeros = int(compressed_text[0])
    # Removing the character that stored the information about 0s added
    compressed_text = compressed_text[1:]
    # Getting the refined compressed text
    compressed_text = refine_text(compressed_text, added_zeros)
    # Decompressing the compressed text finally
    final_string = decompress_text(compressed_text, huffman_code)
    # Returning the final string
    return final_string

TO_CHECK = ''
with open('requirements.txt', 'r', encoding='utf8') as f:
    TO_CHECK = f.read()
check_string = cstw(TO_CHECK)
code, text = separate_huffman_codes_and_text(check_string)
zeros = int(text[0])
text = text[1:]
original_size = len(TO_CHECK)
compressed_size = len(check_string)
compressed_size_without_code = len(text)
text = refine_text(text, zeros)
new_text = decompress_text(text, code)
print_string = f"""
LOSSLESS CONVERSION                       = {"Yes" if TO_CHECK == new_text else "No"}
Original size                             = {original_size}\tBytes
Compression size (without the dictionary) = {compressed_size_without_code}\tBytes
Compression size (with the dictionary)    = {compressed_size}\tBytes
Compression rate (without the dictionary) = {(((original_size - compressed_size_without_code)/original_size)*100):.3f} %
Compression rate (with the dictionary)    = {(((original_size - compressed_size)/original_size)*100):.3f} %
Bytes saved                               = {(original_size - compressed_size)}\tBytes
"""
print(print_string)
# print(new_text)