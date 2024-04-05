import subprocess
import sys
from pathlib import Path

def write_output_to_file(output, file_name):
    """
    Writes the given output to a file.

    Args:
        output: The output to write to the file.
        file_name: The name of the file to write to.
    """
    with open(file_name, "w") as file:
        file.write(output)

def remove_extension(file_name):
    """
    Removes the file extension from a file name.

    Args:
        file_name: The file name to process.

    Returns:
        The file name with the extension removed.
    """
    return file_name.stem

def run_cpp_code(cpp_file, args=[]):
    """
    Compiles and runs C++ code using the subprocess module.

    Args:
        cpp_file: Path to the C++ source file.
        args: List of arguments to pass to the executable.

    Returns:
        The captured output of the C++ program as a string, 
        or None if an error occurs during compilation or execution.
    """    

    # Compile the C++ code
    try:
        exe_name = remove_extension(cpp_file) + ".exe"
        subprocess.run(["g++", str(cpp_file), "-o", str(exe_name)], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error: Compilation failed: {e}")
        return None

    # Run the compiled executable
    try:
        result = subprocess.run([str(exe_name)] + args, cwd=Path.cwd(), capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode
    
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None


    
    
def main():
    folder_structure = ["test"]
    cpp_file = "helloworld.cpp"
    
    # Construct the full path using pathlib.Path
    script_path = Path.cwd()
    for folder in folder_structure:
        script_path = script_path / folder
        
    script_path = script_path / cpp_file
    print('HERE IS WHAT IM DOING')
    print(script_path)
    
    # Check if the file exists before attempting to run it
    if script_path.exists():
        run_cpp_code(script_path)
    else:
        print("Error: C++ file not found.")
        return


main()
