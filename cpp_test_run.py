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

  # Compile the C++ code (replace 'g++' with your compiler if necessary)
  try:
    subprocess.run(["g++", cpp_file, "-o", "hw1.exe"], check=True)
    
  except subprocess.CalledProcessError:
    print("Error: Compilation failed")
    return None

  # Run the compiled executable
  try:
    result = subprocess.run(["./hw1.exe"] + args, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode
  except subprocess.CalledProcessError as e:
    print("Error:", e)
    return None

# Example usage:
cpp_code_file = "hw1.cpp"
arguments = ["gettysburg_address.txt", "out.txt", "4", "flush_right"]

output = run_cpp_code(cpp_code_file, arguments)

if output[0]:
  print("C++ program output:")
  print(output[0])
  
elif output[1]:
  print(f"An error occurred while running {cpp_code_file}: {output[1]}")

elif output[2] != 0:
  print(f"An error occurred while running {cpp_code_file}: UNKNOWN ERROR!")
  
else:
  print(f"Successfully ran {cpp_code_file} with no output. Check output file")