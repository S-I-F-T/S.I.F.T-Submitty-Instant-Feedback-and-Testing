import subprocess

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
    return result.stdout, result.stderr
  except subprocess.CalledProcessError as e:
    print("Error:", e)
    return None

# Example usage:
cpp_code_file = "hw1.cpp"
arguments = ["arg1", "arg2"]

output = run_cpp_code(cpp_code_file, arguments)

if output[0]:
  print("C++ program output:")
  print(output[0])
  
elif output[1]:
  print(f"An error occurred while running {cpp_code_file}: {output[1]}")

else:
  print(f"An error occurred while running {cpp_code_file}: UNKNOWN ERROR!")