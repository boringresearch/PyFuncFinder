import os
from src.find_function_definition import find_function_definition_str

def test_find_function_definition_str():
    # Create a temporary directory with a sample Python file
    temp_dir = 'temp_python_files/'
    os.makedirs(temp_dir, exist_ok=True)
    
    sample_function = "def add(a, b):\n    return a + b"
    
    with open(f"{temp_dir}sample_file.py", 'w', encoding='utf-8') as f:
        f.write(f"# This is a sample Python file\n\n{sample_function}\n")
    
    result = find_function_definition_str(temp_dir, 'add')
    assert result == sample_function
