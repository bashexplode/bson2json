#!/usr/bin/env python3
import argparse
import bson
from bson import json_util

def convert_bson_to_json(input_file, output_file):
    # Open the BSON file in binary mode and decode all documents
    with open(input_file, 'rb') as f:
        # bson.decode_all returns a list of documents
        documents = bson.decode_all(f.read())
    
    # Convert the list of documents to a JSON formatted string using json_util
    json_str = json_util.dumps(documents, indent=4)
    
    # Write the JSON string to the output file
    with open(output_file, 'w') as f:
        f.write(json_str)
    
    print(f"Successfully converted {input_file} to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert a BSON file to a JSON file.")
    parser.add_argument("input_file", help="Path to the input BSON file")
    parser.add_argument("output_file", help="Path to the output JSON file")
    args = parser.parse_args()

    convert_bson_to_json(args.input_file, args.output_file)

if __name__ == '__main__':
    main()
