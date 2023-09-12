def read_file_lines(file_path: str) -> list:
    """Reads a file and returns its lines as a list."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    except Exception as e:
        return None

def find_function_in_lines(lines: list, function_name: str) -> str:
    """Finds the function definition within a list of code lines."""
    inside_function = False
    function_lines = []
    indentation = 0
    
    for line in lines:
        stripped_line = line.strip()
        
        if stripped_line.startswith(f"def {function_name}("):
            inside_function = True
            indentation = len(line) - len(stripped_line)
            
        if inside_function:
            function_lines.append(line.rstrip())
            
        if inside_function and stripped_line:
            current_indentation = len(line) - len(stripped_line)
            if current_indentation < indentation:
                break
                
    return "\n".join(function_lines) if function_lines else None

def find_function_definition_str(folder_path: str, function_name: str) -> str:
    """Searches for the definition of a function in Python files within a given folder."""
    import os
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                lines = read_file_lines(file_path)
                
                if lines:
                    function_str = find_function_in_lines(lines, function_name)
                    if function_str:
                        return function_str
    
    return f"Function {function_name} not found."

