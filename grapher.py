from lorem_text import lorem
from compressor import create_string_to_write as compress
from decompressor import create_string_to_write as decompress
from time import perf_counter

bytes_saved = []
file_size = []
compressed_file_size = []
paragraphs = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
compression_times = []
decompression_times = []

def convert_number_to_readable(n: int) -> str:
    readable = ''
    neg = False
    if n < 0:
        n = -n
        neg = True
    readable += f'{f'{n%1000:03d}' if n//1000 > 0 else f'{n%1000}'}'
    n//=1000
    while n:
        readable = f'{f'{(n)%1000:03d}' if n//1000 > 0 else f'{n%1000}'},' + readable
        n//=1000
    return readable if not neg else ('-' + readable)


for i in paragraphs:
    start = perf_counter()
    x = lorem.paragraphs(i)
    end = perf_counter()
    print(f'Time taken to generate {i} paragraphs = {((end - start)*1000):.3f} ms')
    start = perf_counter()
    compressed = compress(x)
    end = perf_counter()
    compression_times.append(f'{((end - start)*1000):.3f} ms')
    start = perf_counter()
    new_text = decompress(compressed)
    end = perf_counter()
    decompression_times.append(f"{((end - start)*1000):.3f} ms")
    print(f"{i} : {new_text==x}")
    file_size.append((len(x)))
    bytes_saved.append(((len(x)- len(compressed))))
    compressed_file_size.append((len(compressed)))

percentages = [f'{((bytes_saved[i] / file_size[i])*100):.03f} %' for i in range(len(paragraphs))]
rows = [0]*len(paragraphs)
headers = ['Number of Paragraphs', 
           'Original File size\n(Bytes)', 
           'File Size after compression\n(Bytes)', 
           'Amount of Bytes saved\n(Bytes)', 
           'Percentage of\nfile size Saved', 
           'Compression Time', 
           'Decompression Time']
for i in range(len(paragraphs)):
    rows[i] = [convert_number_to_readable(paragraphs[i]), 
               convert_number_to_readable(file_size[i]), 
               convert_number_to_readable(compressed_file_size[i]), 
               convert_number_to_readable(bytes_saved[i]), 
               percentages[i], 
               compression_times[i], 
               decompression_times[i]]

from tabulate import tabulate

table = tabulate(rows, headers, 'pipe', floatfmt='.03f', numalign='right', stralign='right', showindex='always')
print(table)