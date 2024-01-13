from huffman_tree import generate_tree_from_code
from nodes import LeafNode, TreeNode
from analyser import str_rep, is_valid_dict
from imports import loads, JSONDecodeError
from exception_handler import DecimalToBinaryExpectedIntException, DecimalToBinaryNegativeIntException
from exception_handler import TextCorruptedExpection, SeparateHuffmanCodesExpectedStringException
from exception_handler import RefineTextExpectedIntException, DecompressTextExpectedStringException
from exception_handler import RefineTextExpectedStringException, DecompressTextDictStructureException
from exception_handler import DecompressTextExpectedDictException, CreateStringToWriteExpectedStringException

# This function will convert a decimal number to binary (only positive numbers)
# Return type -> str
def decimal_to_binary(deci: int) -> str:

    # If the number provided is not an integer, raise proper error
    if not isinstance(deci, int):
        raise DecimalToBinaryExpectedIntException(f"""
Function Call : decimal_to_binary({deci = })
Provided value {deci = } is not an integer.
""")

    # If the number provided is less than 0, raise proper error
    if deci < 0:
        raise DecimalToBinaryNegativeIntException(f"""
Function Call : decimal_to_binary({deci = })
Provided value {deci = } is a negative number, while the function only takes positive values.
""")

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
    del mod8, deci
    return binary # if mod 8 was 0 we just return the string as it is

# This function will separate huffman codes and the compressed string from text provided
# Return type -> tuple [ dict [ str : int ] , str ]
def separate_huffman_codes_and_text(text: str) -> tuple[dict[str: int], str]:
    
    # If the text provided is not a string literal, raise proper error
    if not isinstance(text, str):
        raise SeparateHuffmanCodesExpectedStringException(f"""
Function Call : separate_huffman_codes_and_text({text = })
Provided value {text = } is not a string literal.
""")

    # creating an empty string and dictionary
    compressed_text = ''
    huffman_codes = dict()
    
    # searching the string from behind and capturing exactly where the codes start
    for i in range(len(text)-1, -1, -1):
        if text[i]=='\n':
            if text[i+1] == '{':
                # convert the codes back from string to dict
                try:
                    huffman_codes = loads(text[i+1:])
                except JSONDecodeError:
                    raise TextCorruptedExpection("separate_huffman_codes_and_text()", f"""
Function Call : separate_huffman_codes_and_text({text = })

Provided value {text = }\n\nHas modified the codes required for decompression attached at the end and hence has been rendered corrupted.
""")
                # add the rest of the string as the compressed string
                compressed_text = text[:i]
                break
    else:
        raise TextCorruptedExpection("separate_huffman_codes_and_text()", f"""
Function Call : separate_huffman_codes_and_text({text = })


Provided value {text = }\n\nIs missing codes required for decompression hence has been rendered corrupted.
""")
    del text
    # Returning a tuple of the codes and compressed text
    return huffman_codes, compressed_text

# This function will remove added zeros during compression and
# convert the text from 8 bit unicode to 8 bit binary
# Return type -> str
def refine_text(compressed_text_from_file: str, added_zeros: int) -> str:
    
    # If added zeros is not an integer, raise proper error
    if not isinstance(added_zeros, int):
        raise RefineTextExpectedIntException(f"""
Function Call : refine_text(

{compressed_text_from_file = }

,{added_zeros = })

Provided Value {added_zeros = } is not an integer.
""")
    
    # If added zeros is out of expected range, raise proper error
    if added_zeros < 0 or added_zeros > 7:
        raise TextCorruptedExpection("refine_text()", f"""
Function Call : refine_text(

{compressed_text_from_file = }

,{added_zeros = })

Provided Value {added_zeros = } is not in the range (0, 7) hence the file has been rendered corrupt.
""")
    
    # If compressed text from file is not a string, raise proper error
    if not isinstance(compressed_text_from_file, str):
        raise RefineTextExpectedStringException(f"""
Function Call : refine_text(

{compressed_text_from_file = }

,{added_zeros = })

Provided Value 

{compressed_text_from_file = }

is not a string literal.
""")

    # creating an empty string
    refined_text = ''
    # looping over the text
    for i in compressed_text_from_file:
        # convert the unicode character to decimal and the decimal to binary string
        refined_text += decimal_to_binary_8_bit(ord(i))
    
    # If the number of 0s to remove is more than the length of the string to remove them from,
    # raise proper error
    if len(refined_text) <= added_zeros:
        raise TextCorruptedExpection("refine_text()", f"""
Function Call : refine_text({compressed_text_from_file = }, {added_zeros = })

Provided text after converting to binary {refined_text} has less digits than the number of 0s to be removed. 
Rendering it corrupted.
""")
    
    # If the substring has non 0 values where 0s should have been, raise proper error
    for i in refined_text[:added_zeros]:
        if i == '1':
            raise TextCorruptedExpection("refine_text()", f"""
Function Call : refine_text(
{compressed_text_from_file = },\n{added_zeros = })
Provided text after converting to binary\n{refined_text}\nhas non-zeros in the part where zeros should have been placed.
Rendering it corrupted.
""")
    del compressed_text_from_file
    # Removing the added zeros
    refined_text = refined_text[added_zeros:]
    del added_zeros
    # Returning our refined string
    return refined_text

# This function will decompress the refined text based on the codes provided
# Return type -> str
def decompress_text(text: str, code: dict[str : str]) -> str:
    
    str_rep_code = str_rep(code)
    # If the text provided is not a string, raise proper error
    if not isinstance(text, str):
        raise DecompressTextExpectedStringException(f"""
Function Call : decompress_text({text = }, code = {str_rep_code})
Provided Value {code = } is not a dictionary.
""")
    
    code_validity = is_valid_dict(code, key_type=str, value_type=str)
    # If the dictionary is not valid, raise proper exception
    if not code_validity[0]:
        if len(code_validity) == 2:
            key, value = code_validity[1]
            raise DecompressTextDictStructureException(f"""
Function Call : decompress_text({text = }, codes = {str_rep_code})
The Pair {key = }, {value = } in code does not match the requirements (key: str, value: str).
""")
        raise DecompressTextExpectedDictException(f"""
Function Call : decompress_text({text = }, {code = })
Provided Value {code = } is not a dictionary.
""")
    
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
    
    # If the last character didn't lead to the final leaf node, raise proper error
    if pointer is not huffman_tree:
        raise TextCorruptedExpection('decompress_text()', f"""
Function Call : decompress_text({text = }, code = {str_rep(code)})


Provided value {text = }\n\ncouldn't lead to an end. Hence it is rendered corrupt.
""")
    del huffman_tree, code, text, pointer
    # Return the decompressed text
    return decompressed_text

# This function will call all the necessary functions 
# and create the final string to be written in the output file
# Return type -> str
def create_string_to_write(text: str) -> str:
    
    # If the text provided is not a string, raise proper error
    if not isinstance(text, str):
        raise CreateStringToWriteExpectedStringException(f"""
Fuunction Call : create_string_to_write({text = })
Provided Value {text = } is not a string.
""")
    
    # Separating and storing the code and compressed text
    huffman_code, compressed_text = separate_huffman_codes_and_text(text)
    # Retrieving the number of zeros that were added during compression
    try:
        added_zeros = int(compressed_text[0])
    except:
        raise TextCorruptedExpection(f"""
Function Call : create_string_to_write(
{text = }
)

Provided text had non-integer value the 0th index. Hence, number of zeros added is unknown.
Rendering the text as corrupted.

""")
    # Removing the character that stored the information about 0s added
    compressed_text = compressed_text[1:]
    # Getting the refined compressed text
    compressed_text = refine_text(compressed_text, added_zeros)
    # Decompressing the compressed text finally
    final_string = decompress_text(compressed_text, huffman_code)
    del compressed_text, huffman_code, added_zeros, text
    # Returning the final string
    return final_string