Here's the content you can directly paste into your README.md file for GitHub:

markdown
# Smart Code Documentation Generator

A Python-based tool designed to automatically generate well-structured markdown documentation for codebases. The tool traverses through directories containing multiple Python files, extracts functions, classes, and other relevant details, and produces a cohesive documentation file.

## Features

- **Automatic Parsing**: Scans a directory and extracts information about functions, classes, and imports.
- **Comprehensive Documentation**:
  - Supports both detailed and brief styles of documentation.
  - Generates a Table of Contents for easy navigation.
- **Handles Multiple Files**: Works seamlessly with codebases containing multiple Python files.
- **Error Handling**: Gracefully manages exceptions and reports issues with problematic files.

## How It Works

1. **Directory Parsing**:
   - Recursively scans a specified directory to find all Python files.
   - Extracts module-level docstrings, functions, classes, imports, and other metadata.

2. **Documentation Generation**:
   - Creates a markdown file with a structured format, including docstrings, function signatures, class definitions, and more.
   - Provides options for different styles of documentation: detailed (including all information) and brief (key details only).

## Installation

1. Clone the repository:
   
   git clone https://github.com/AshwinSaklecha/smart-doc-generator.git
   
2. Navigate into the project directory:
   bash
   cd smart-doc-generator
   
3. Install the required dependencies: os, ast, inspect, typing
   

## Usage

1. Update the `directory_path` in the script to point to your codebase:
   python
   directory_path = "path_to_your_codebase"
   
2. Run the script:
   bash
   python main.py
   
3. View the generated documentation:
   - The markdown file `documentation.md` will be created in the project directory.

## Options

### Documentation Style:

- `brief`: Only essential information (default).
- `detailed`: Complete information, including imports, decorators, and docstrings.

You can switch styles by passing `style="detailed"` or `style="brief"` to the `generate_documentation` function.

## Example

Here's an example of how to use the tool in your script:

python
directory_path = "D:\\megaProject\\codeFiles"  # Use raw string or escape backslashes
functions_and_classes = parse_code_from_directory(directory_path)
generate_documentation(functions_and_classes, style="brief")  # or "detailed"


## Contributing

Feel free to open issues or submit pull requests for improvements and new features. All contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- Python **AST module** for parsing and analyzing the code.
- The open-source community for tools and libraries that made this project possible.

<!-- 
### Notes:
- Replace yourusername in the repository URL with your actual GitHub username.
- Make sure that requirements.txt is properly defined in your project to include all dependencies. -->
