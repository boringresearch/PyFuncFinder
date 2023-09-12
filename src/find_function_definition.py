def find_function_definition_str(folder_path: str, function_name: str) -> str:
    import os

    def search_function_in_file(file_path: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                inside_function = False
                function_lines = []
                for line in lines:
                    line = line.strip()
                    if line.startswith(f"def {function_name}("):
                        inside_function = True
                    if inside_function:
                        function_lines.append(line)
                    if inside_function and line == "":
                        break
                if function_lines:
                    return "\n".join(function_lines)
        except Exception as e:
            return None

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                function_str = search_function_in_file(file_path)
                if function_str:
                    return function_str
                    
    return f"Function {function_name} not found."
