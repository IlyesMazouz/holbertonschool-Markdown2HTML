#!/usr/bin/python3
"""
Converts Markdown file to HTML

This script takes two command-line arguments: the input Markdown file and the
output HTML file. It uses the 'markdown' library to perform the conversion.
"""

import sys
import os
import markdown


def convert_markdown_to_html(input_file, output_file):
    try:
        with open(input_file, "r") as md_file:
            md_content = md_file.read()
            html_content = markdown.markdown(md_content)

        with open(output_file, "w") as html_file:
            html_file.write(html_content)

        return 0
    except FileNotFoundError:
        print(f"Missing {input_file}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    exit_code = convert_markdown_to_html(input_file, output_file)

    sys.exit(exit_code)
