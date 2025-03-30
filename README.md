# BSON to JSON Converter

This repository contains a simple Python script that converts a BSON file into a JSON file. It leverages the PyMongo BSON library to handle BSON-specific types and provides a command-line interface for ease of use.

## Features

- **Simple Conversion:** Reads BSON files and outputs the equivalent JSON formatted data.
- **BSON-Specific Handling:** Utilizes PyMongo's `json_util` to correctly handle BSON-specific types.
- **Command-Line Interface:** Accepts input and output file paths as command-line arguments.

## Requirements

- Python 3.x
- [PyMongo](https://pypi.org/project/pymongo/) (Install via pip)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bashexplode/bson2json.git
   ```

2. **Navigate to the repository directory:**
   ```bash
   cd bson2json
   ```

3. **Install the required dependencies:**
   ```bash
   pip install pymongo
   ```

## Usage

The script is named `bson2json.py` and requires two arguments: the input BSON file and the output JSON file.

### Example

```bash
python bson2json.py input.bson output.json
```

This command reads `input.bson`, converts its contents into JSON format, and writes the output to `output.json`.

## How It Works

- **Command-line Arguments:** Uses Python's `argparse` module to handle input and output file paths.
- **BSON Decoding:** Opens the BSON file in binary mode and decodes all contained documents using `bson.decode_all`.
- **JSON Conversion:** Converts the decoded BSON documents into a JSON string using `json_util.dumps`, ensuring BSON-specific data types are properly handled.
- **File Output:** Writes the resulting JSON string to the specified output file.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

idc use this for whatever

---
