#!/bin/bash

# Check if the input file is provided
if [ $# -ne 1 ]; then
  echo "Usage: ./run.sh <input_file>"
  exit 1
fi

# Run the Python lexer program with input from the specified file
python3 lexer.py3 < "$1"

