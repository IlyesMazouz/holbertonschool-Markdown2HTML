#!/usr/bin/python3
"""
This script takes two command-line arguments: the input Markdown file and the
output HTML file. It uses the 'markdown' library to perform the conversion
from md to HTML
"""

import sys
import os
import markdown

def convert_markdown_to_html(input_file, output_file):
    """
    Converts Markdown file to HTML
    """
    try:
        # read Markdown content from the input file
        with open(input_file, 'r') as md_file:
            md_content = md_file.read()
            # convert Markdown to HTML
            html_content = markdown.markdown(md_content)

        # write the HTML content to the output file
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

        return 0
    except FileNotFoundError:
        # handle the case where the input file is not found
        print(f"Missing {input_file}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    # check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # extract input and output file names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # perform the Markdown to HTML conversion
    exit_code = convert_markdown_to_html(input_file, output_file)

    # exit with the appropriate exit code
    sys.exit(exit_code)
