from printer import print_error, Fore, Style
class HuffmanExceptions(Exception):
    def __init__(self, *args: object) -> None:
        print_error(f"Exception Name : {type(self).__name__} - {args[0]}{Style.RESET_ALL}", end=f'\n{Fore.CYAN}')
        super().__init__(*args)
    
class AnalyserExceptions(HuffmanExceptions):
    def __init__(self, *args: object) -> None:
        print_error('The function was part of the analyser.py file.')
        super().__init__(*args)
    
class CountLettersExpectedStringException(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling the count_letters() function.')
        super().__init__(*args)

class SeparatorSplitExpectedStringExpection(AnalyserExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling separator_split() function.')
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

class CompressorExceptions(HuffmanExceptions):
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

class DecompressorExceptions(HuffmanExceptions):
    def __init__(self, *args: object) -> None:
        print_error('The Function was part of the decompressor.py file.')
        super().__init__(*args)

class DecimalToBinaryExpectedIntException(DecompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling decimal_to_binary() function.')
        super().__init__(*args)

class DecimalToBinaryNegativeIntException(DecompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling decimal_to_binary() function.')
        super().__init__(*args)

class DecompressTextDictStructureException(DecompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling decompress_text() function.')
        super().__init__(*args)

class SeparateHuffmanCodesExpectedStringException(DecompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling separate_huffman_codes_and_text() function.')
        super().__init__(*args)

class RefineTextExpectedStringException(DecompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling refine_text() function.')
        super().__init__(*args)

class RefineTextExpectedIntException(DecompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling refine_text() function.')
        super().__init__(*args)

class DecompressTextExpectedStringException(DecompressorExceptions):
    def __init__(self, *args: object) -> None:    
        print_error('Error occurred while calling decompress_text() function.')
        super().__init__(*args)

class DecompressTextExpectedDictException(DecompressorExceptions):
    def __init__(self, *args: object) -> None:    
        print_error('Error occurred while calling decompress_text() function.')
        super().__init__(*args)

class CreateStringToWriteExpectedStringException(DecompressorExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling create_string_to_write() function.')
        super().__init__(*args)

class TextCorruptedExpection(DecompressorExceptions):
    def __init__(self, function_name: str, *args: object) -> None:
        print_error(f'Error occurred while calling {function_name} function.')
        super().__init__(*args)

class HuffmanTreeExceptions(HuffmanExceptions):
    def __init__(self, *args: object) -> None:
        print_error('The Function was part of the huffman_tree.py file.')
        super().__init__(*args)

class GenerateTreeExpectedDictException(HuffmanTreeExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling generate_tree_from_code() function.')
        super().__init__(*args)

class GenerateTreeDictStructureException(HuffmanTreeExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling generate_tree_from_code() function.')
        super().__init__(*args)

class MakeJunctionTreeEmptyQueueException(HuffmanTreeExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling make_junction_tree() function.')
        super().__init__(*args)

class MakeJunctionTreeExpectedQueueException(HuffmanTreeExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling make_junction_tree() function.')
        super().__init__(*args)

class ConvertJunctionToTreeExpectedJunctionNodeException(HuffmanTreeExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling convert_junction_to_tree() function.')
        super().__init__(*args)

class GetHuffmanCodesExpectedTreeNodeException(HuffmanTreeExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling get_huffman_codes() function.')
        super().__init__(*args)

class GetHuffmanCodesExpectedStringException(HuffmanTreeExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling get_huffman_codes() function.')
        super().__init__(*args)

class GenerateCodeFromQueueExpectedQueueException(HuffmanTreeExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling generate_code_from_queue() function.')
        super().__init__(*args)

class GenerateCodeFromQueueEmptyQueueException(HuffmanTreeExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred while calling generate_code_from_queue() function.')
        super().__init__(*args)

class QueuesExceptions(HuffmanExceptions):
    def __init__(self, *args: object) -> None:
        print_error('The Function was part of the queues.py file.')
        super().__init__(*args)

class NonIntegerQueueSizeException(QueuesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when setting the size of the queue.')
        super().__init__(*args)

class NegativeQueueSizeException(QueuesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when setting the size of the queue.')
        super().__init__(*args)

class QueueIndexOutOfRangeException(QueuesExceptions):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class QueueIndexExpectedIntException(QueuesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when accessing an element of the queue.')
        super().__init__(*args)

class QueueItemExpectedStringJunctionNodeException(QueuesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when setting an item in the queue to a value.')
        super().__init__(*args)

class EmptyQueueException(QueuesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when dequeueing an empty queue.')
        super().__init__(*args)

class NodesExceptions(HuffmanExceptions):
    def __init__(self, *args: object) -> None:
        print_error('The Function was part of the nodes.py file.')
        super().__init__(*args)

class NextNodeExpectedStringOrJunctionNodeOrNoneException(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when trying to set the next node to the current node.')
        super().__init__(*args)

class PreviousNodeExpectedQueueNodeOrNoneException(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when trying to set the previous node to the current node.')
        super().__init__(*args)

class RootNodePreviousExpectedNoneException(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when trying to set the previous node to a root node.')
        super().__init__(*args)

class AttemptedRootNodeAdditionException(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when trying to add a root node to something.')
        super().__init__(*args)

class OperandExpectedStringOrJunctionNode(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when trying to add a node to something.')
        super().__init__(*args)

class NodeValueExpectedStringException(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when setting the value of a node.')
        super().__init__(*args)

class NodeValueEmptyException(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when setting the value of a node.')
        super().__init__(*args)

class NodeStrengthExpectedIntException(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when trying to set the strength of a node.')
        super().__init__(*args)

class NodeStrengthExpectedGreaterThan1Exception(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when trying to set the strength of a node.')
        super().__init__(*args)

class NodeChildrenExpectedTupleException(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when trying to set the children of a node.')
        super().__init__(*args)

class NodeChildrenStructureException(NodesExceptions):
    def __init__(self, *args: object) -> None:
        print_error('Error occurred when trying to set the children of a node.')
        super().__init__(*args)