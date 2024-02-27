import subprocess

def remove_extension(file_name):
  """
  Removes the file extension from a file name.

  Args:
    file_name: The file name to process.

  Returns:
    The file name with the extension removed.
  """
  return file_name[:file_name.rfind(".")]

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
    exec_name = remove_extension(cpp_file) + ".exe"
    
    # Compile the C++ code (replace 'g++' with your compiler if necessary)
    try:
        subprocess.run(["g++", cpp_file, "-o", f"{exec_name}"], check=True)

    except subprocess.CalledProcessError:
        print("Error: Compilation failed")
        return None

   

    # Run the compiled executable
    try:
        result = subprocess.run([f"./{exec_name}"] + args, capture_output=True, text=True)
        return result.stdout, result.stderr, result.returncode

    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None

# Test the run_cpp_code function

def main():
  
    cpp_code_file = "hw1.cpp"
    arguments = ["gettysburg_address.txt", "out.txt", "4", "flush_right"]

    output = run_cpp_code(cpp_code_file, arguments)

    if output[0]:
        print("C++ program output:\n")
        print(output[0])

    elif output[1]:
        print(f"An error occurred while running {cpp_code_file}: {output[1]}")

    # Unknown error because program exited with a non-zero status
    elif output[2] != 0:
        print(f"An error occurred while running {cpp_code_file}: UNKNOWN ERROR!")

    # No output, but check the output file
    else:
        print(f"Successfully ran {cpp_code_file} with no output. Check output file")
    
if __name__ == "__main__":
    main()