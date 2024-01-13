from lorem_text import lorem
from compressor import create_string_to_write
from decompressor import create_string_to_write as dc_create_string_to_write
from time import perf_counter

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
compressed_file_size = []
paragraphs = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

for i in paragraphs:
    start = perf_counter()
    x = lorem.paragraphs(i)
    end = perf_counter()
    print(f'Time taken to generate {i} paragraphs = {((end - start)*1000):.3f} ms')
    start = perf_counter()
    compressed = create_string_to_write(x)
    file_size.append(len(x))
    bytes_saved.append(len(x)- len(compressed))
    compressed_file_size.append(len(compressed))
    end = perf_counter()
    print(f'Time taken to compress {i} paragraphs = {((end - start)*1000):.3f} ms')
    start = perf_counter()
    new_text = dc_create_string_to_write(compressed)
    end = perf_counter()
    print(f'Time taken to decompress {i} paragraphs = {((end - start)*1000):.3f} ms')
    print(f"{i} : {new_text==x}")

percentages = [f'{((bytes_saved[i] / file_size[i])*100):.03f}' for i in range(len(paragraphs))]

rows = [0]*len(paragraphs)

for i in range(len(paragraphs)):
    rows[i] = [percentages[i], bytes_saved[i], file_size[i], compressed_file_size[i]]

from tabulate import tabulate

table = tabulate(rows, ['Percentage of file size Saved', 'Amount of Bytes saved', 'Original File size', 'File Size after compression'])
print(table)