from matplotlib import pyplot as plt
from lorem_text import lorem
from compressor import create_string_to_write
from decompressor import separate_huffman_codes_and_text, refine_text, decompress_text

# def __str__(self, level=0) -> str:
#     to_return = "\t" * level + self.__repr__() + "\n" + '\t' * level + '{\n'
#     for child in self.children:
#         if child.type == LeafNode:
#             to_return += "\t" * (level + 1) + child.value + "\n"
#         else:
#             to_return += child.__str__(level+1)
#     return to_return + '\t' * level + '}\n'

bytes_saved = []
file_size = []

paragraphs = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for i in paragraphs:
    x = lorem.paragraphs(i)
    compressed = create_string_to_write(x)
    code, text = separate_huffman_codes_and_text(compressed)
    zeros = int(text[0])
    text = text[1:]
    bytes_saved.append(len(x) - len(compressed))
    file_size.append(len(x))
    text = refine_text(text, zeros)
    new_text = decompress_text(text, code)
    print(f"{i} : {new_text==x}")

percentages = [f'{((bytes_saved[i] / file_size[i])*100):.3f} %' for i in range(len(paragraphs))]
print(percentages)
print(bytes_saved)
print(file_size)
plt.plot(bytes_saved, file_size, label='Bytes Saved Through Huffman Encoding')
plt.xlabel('File Size (in Bytes)')
plt.ylabel('Bytes Saved')
plt.title('Huffman Encoding Results')
plt.legend()
plt.show()