import os
import ast

def parse_code_from_directory(directory_path):
    all_functions = []
    all_classes = []

    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Only process Python files
        if filename.endswith(".py"):
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
            
            # Add the functions and classes to the global lists
            all_functions.append({"file": filename, "functions": functions})
            all_classes.append({"file": filename, "classes": classes})

    return all_functions, all_classes

# Example usage
# directory_path = "your_code_directory"  # Replace with the path to your code directory
# functions, classes = parse_code_from_directory(directory_path)
# print(f"Functions: {functions}")
# print(f"Classes: {classes}")
