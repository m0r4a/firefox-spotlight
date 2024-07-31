import lz4.block
from sys import argv
import json


def read_jsonlz4_file(file_path):
    with open(file_path, 'rb') as file:
        # The first 8 bytes are a custom header specific to Mozilla, skip them
        file.read(8)
        compressed_data = file.read()

    decompressed_data = lz4.block.decompress(compressed_data)
    json_data = json.loads(decompressed_data)

    return json_data


file_path = argv[1]
data = read_jsonlz4_file(file_path)
print(json.dumps(data, indent=4))  # Pretty-print the JSON data
