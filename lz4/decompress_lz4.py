import lz4.block
from sys import argv
import json
from re import search


def main():
    read_jsonlz4_file()


def read_jsonlz4_file():

    file_path = argv[1]

    file_path_validator(file_path)

    with open(file_path, 'rb') as file:
        # The first 8 bytes are a custom header specific to Mozilla, skip them
        file.read(8)
        compressed_data = file.read()

    decompressed_data = lz4.block.decompress(compressed_data)
    json_data = json.loads(decompressed_data)

    return json_data


def file_path_validator(file_path):
    if not search(r".*bookmarks.*\.jsonlz4$", file_path):
        raise ValueError("File is not a .jsonlz4 file")


if __name__ == '__main__':
    data = read_jsonlz4_file()
    print(json.dumps(data, indent=4))
