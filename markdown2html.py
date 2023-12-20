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
    """
    Converts Markdown file to HTML.

    Args:
        input_file (str): Path to the input Markdown file.
        output_file (str): Path to the output HTML file.

    Returns:
        int: Exit code (0 for success, 1 for failure).
    """
    try:
        # Read Markdown content from the input file
        with open(input_file, "r") as md_file:
            md_content = md_file.read()
            # Convert Markdown to HTML
            html_content = markdown.markdown(md_content)

        # Write the HTML content to the output file
        with open(output_file, "w") as html_file:
            html_file.write(html_content)

        return 0
    except FileNotFoundError:
        # Handle the case where the input file is not found
        print(f"Missing {input_file}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    # Extract input and output file names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Perform the Markdown to HTML conversion
    exit_code = convert_markdown_to_html(input_file, output_file)

    # Exit with the appropriate exit code
    sys.exit(exit_code)
