import os
import ast

# Function to parse code in a directory and extract function and class details
def parse_code_from_directory(directory_path):
    all_functions_and_classes = []  # This will hold both functions and classes for each file

    # Check if the provided directory exists
    if not os.path.isdir(directory_path):
        raise ValueError(f"The directory {directory_path} does not exist or is not a valid directory.")

    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Only process Python files
        if filename.endswith(".py"):
            try:
                with open(file_path, 'r') as file:
                    code = file.read()

                # Parse the code into an Abstract Syntax Tree (AST)
                tree = ast.parse(code)
                
                # Extract functions and their details
                functions = []
                classes = []
                
                for node in tree.body:
                    if isinstance(node, ast.FunctionDef):
                        function_info = {
                            "name": node.name,
                            "args": [arg.arg for arg in node.args.args],  # Extracting function arguments
                            "docstring": ast.get_docstring(node)  # Extracting docstring
                        }
                        functions.append(function_info)

                    if isinstance(node, ast.ClassDef):
                        class_info = {
                            "name": node.name,
                            "docstring": ast.get_docstring(node)  # Extracting class docstring
                        }
                        classes.append(class_info)
                
                # Add both functions and classes to a single dictionary for each file
                all_functions_and_classes.append({
                    "file": filename,
                    "functions": functions,
                    "classes": classes
                })

            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    return all_functions_and_classes

# Function to generate markdown documentation
def generate_documentation(functions_and_classes, output_file="documentation.md"):
    with open(output_file, 'w') as doc_file:
        # Write a title for the documentation
        doc_file.write("# Project Documentation\n\n")
        
        # Loop through each file's functions and classes and generate documentation
        for file_info in functions_and_classes:
            file_name = file_info["file"]
            doc_file.write(f"## File: {file_name}\n\n")

            # Writing function details
            doc_file.write("### Functions\n")
            for function in file_info["functions"]:
                doc_file.write(f"**Function**: `{function['name']}`\n")
                doc_file.write(f"- **Arguments**: {', '.join(function['args'])}\n")
                doc_file.write(f"- **Docstring**: {function['docstring'] if function['docstring'] else 'No docstring available.'}\n\n")
            
            # Writing class details
            doc_file.write("### Classes\n")
            for class_info in file_info["classes"]:
                doc_file.write(f"**Class**: `{class_info['name']}`\n")
                doc_file.write(f"- **Docstring**: {class_info['docstring'] if class_info['docstring'] else 'No docstring available.'}\n\n")

        print(f"Documentation generated and saved to {output_file}")

# Example usage: You can call this to process the directory and generate documentation
directory_path = "D:\codeFiles"  # Use raw string or escape backslashes
functions_and_classes = parse_code_from_directory(directory_path)
generate_documentation(functions_and_classes)
