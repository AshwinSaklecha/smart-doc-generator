import os
import ast
import inspect
from typing import List, Dict, Any

# Function to parse code in a directory and extract function and class details
def parse_code_from_directory(directory_path):
    all_functions_and_classes = []

    # Check if the provided directory exists
    if not os.path.isdir(directory_path):
        raise ValueError(f"The directory {directory_path} does not exist or is not a valid directory.")

    for root, _, files in os.walk(directory_path):
        for filename in files:
            if not filename.endswith('.py'):
                continue
                
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, directory_path)
            
            try:
                with open(file_path, 'r') as file:
                    code = file.read()
                
                tree = ast.parse(code)
                
                # Extract module-level docstring
                module_doc = ast.get_docstring(tree)
                
                functions = []
                classes = []
                imports = []
                
                for node in tree.body:
                    if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                        imports.extend(_extract_imports(node))
                    elif isinstance(node, ast.FunctionDef):
                        functions.append(_extract_function_info(node))
                    elif isinstance(node, ast.ClassDef):
                        classes.append(_extract_class_info(node))
                
                all_functions_and_classes.append({
                    "file": relative_path,
                    "module_doc": module_doc,
                    "imports": imports,
                    "functions": functions,
                    "classes": classes
                })

            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    return all_functions_and_classes

def _extract_imports(node):
    imports = []
    if isinstance(node, ast.Import):
        for name in node.names:
            imports.append({"name": name.name, "alias": name.asname})
    elif isinstance(node, ast.ImportFrom):
        module = node.module or ''
        for name in node.names:
            imports.append({
                "module": module,
                "name": name.name,
                "alias": name.asname
            })
    return imports

def _extract_function_info(node):
    return {
        "name": node.name,
        "args": _extract_arguments(node.args),
        "returns": _extract_return_annotation(node),
        "docstring": ast.get_docstring(node),
        "decorators": [_extract_decorator(d) for d in node.decorator_list],
        "async": isinstance(node, ast.AsyncFunctionDef),
        "lineno": node.lineno
    }

def _extract_class_info(node):
    methods = []
    attributes = []
    
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            methods.append(_extract_function_info(item))
        elif isinstance(item, ast.AnnAssign):
            attributes.append({
                "name": item.target.id,
                "annotation": _extract_annotation(item.annotation)
            })
    
    return {
        "name": node.name,
        "bases": [_extract_annotation(base) for base in node.bases],
        "docstring": ast.get_docstring(node),
        "methods": methods,
        "attributes": attributes,
        "decorators": [_extract_decorator(d) for d in node.decorator_list],
        "lineno": node.lineno
    }

# Function to generate markdown documentation
def generate_documentation(functions_and_classes, output_file="documentation.md", style="detailed"):
    """
    Generate markdown documentation for the project.
    
    Args:
        functions_and_classes: List of parsed code information
        output_file: Output markdown file path
        style: Documentation style - 'detailed' or 'brief'
    """
    with open(output_file, 'w') as doc_file:
        doc_file.write("# Project Documentation\n\n")
        
        # Generate Table of Contents
        doc_file.write("## Table of Contents\n\n")
        for file_info in functions_and_classes:
            file_name = file_info["file"]
            anchor = file_name.replace('/', '-').replace('.', '-')
            doc_file.write(f"- [{file_name}](#{anchor})\n")
        doc_file.write("\n---\n\n")
        
        # Generate documentation based on style
        for file_info in functions_and_classes:
            file_name = file_info["file"]
            anchor = file_name.replace('/', '-').replace('.', '-')
            
            doc_file.write(f"## {file_name} {{{anchor}}}\n\n")
            
            if file_info["module_doc"] and style == "detailed":
                doc_file.write(f"{file_info['module_doc']}\n\n")
            
            # Document imports only in detailed mode
            if file_info["imports"] and style == "detailed":
                doc_file.write("### Imports\n\n")
                for imp in file_info["imports"]:
                    if "module" in imp:
                        doc_file.write(f"- `from {imp['module']} import {imp['name']}`")
                    else:
                        doc_file.write(f"- `import {imp['name']}`")
                    if imp["alias"]:
                        doc_file.write(f" as `{imp['alias']}`")
                    doc_file.write("\n")
                doc_file.write("\n")
            
            # Document classes
            if file_info["classes"]:
                doc_file.write("### Classes\n\n")
                for class_info in file_info["classes"]:
                    _write_class_documentation(doc_file, class_info, style)
            
            # Document functions
            if file_info["functions"]:
                doc_file.write("### Functions\n\n")
                for function in file_info["functions"]:
                    _write_function_documentation(doc_file, function, style=style)
            
            doc_file.write("---\n\n")

def _write_class_documentation(doc_file, class_info, style="detailed"):
    # Write class header with inheritance
    doc_file.write(f"#### {class_info['name']}")
    if class_info["bases"]:
        bases = ", ".join(class_info["bases"])
        doc_file.write(f" ({bases})")
    doc_file.write("\n\n")
    
    # Write decorators only in detailed mode
    if class_info["decorators"] and style == "detailed":
        doc_file.write("**Decorators:**\n")
        for decorator in class_info["decorators"]:
            doc_file.write(f"- `@{decorator}`\n")
        doc_file.write("\n")
    
    # Write docstring
    if class_info["docstring"] and style == "detailed":
        doc_file.write(f"{class_info['docstring']}\n\n")
    
    # Write attributes only in detailed mode
    if class_info["attributes"] and style == "detailed":
        doc_file.write("**Attributes:**\n\n")
        for attr in class_info["attributes"]:
            doc_file.write(f"- `{attr['name']}: {attr['annotation']}`\n")
        doc_file.write("\n")
    
    # Write methods
    if class_info["methods"]:
        doc_file.write("**Methods:**\n\n")
        for method in class_info["methods"]:
            _write_function_documentation(doc_file, method, is_method=True, style=style)

def _write_function_documentation(doc_file, function, is_method=False, style="detailed"):
    prefix = "- " if is_method else "#### "
    
    # Write function signature
    signature = f"{function['name']}({_format_arguments(function['args'])})"
    if function["returns"]:
        signature += f" -> {function['returns']}"
    
    doc_file.write(f"{prefix}`{signature}`\n\n")
    
    # Write decorators only in detailed mode
    if function["decorators"] and not is_method and style == "detailed":
        doc_file.write("**Decorators:**\n")
        for decorator in function["decorators"]:
            doc_file.write(f"- `@{decorator}`\n")
        doc_file.write("\n")
    
    # Write docstring only in detailed mode
    if function["docstring"] and style == "detailed":
        doc_file.write(f"{function['docstring']}\n\n")

# Helper functions for extraction and formatting
def _extract_arguments(args):
    # Implementation for argument extraction
    pass

def _extract_return_annotation(node):
    # Implementation for return annotation extraction
    pass

def _extract_annotation(node):
    # Implementation for type annotation extraction
    pass

def _extract_decorator(node):
    # Implementation for decorator extraction
    pass

def _format_arguments(args):
    # Implementation for argument formatting
    pass

# Example usage: You can call this to process the directory and generate documentation
directory_path = "D:\megaProject\codeFiles"  # Use raw string or escape backslashes
functions_and_classes = parse_code_from_directory(directory_path)
generate_documentation(functions_and_classes, style="brief")  # or "detailed"
