import ast

def parse_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    # Parse the code into an Abstract Syntax Tree (AST)
    tree = ast.parse(code)
    
    # Extract functions and classes
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    
    # Print the extracted components
    print(f"Found {len(functions)} functions and {len(classes)} classes in {file_path}")
    return functions, classes

# Example usage
# file_path = "example.py"  # Replace with the path to your Python file
# functions, classes = parse_code(file_path)

