import ast

def parse_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    # Parse the code into an Abstract Syntax Tree (AST)
    tree = ast.parse(code)
    
    functions = []
    classes = []
    
    # Extract functions and their details
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
    
    # Output results
    return functions, classes

# Example usage
file_path = "example.py"  # Replace with the path to your Python file
functions, classes = parse_code(file_path)
print(f"Functions: {functions}")
print(f"Classes: {classes}")
