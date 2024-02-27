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
    subprocess.run(["g++", cpp_file, "-o", "cpp_executable"], check=True)
    
  except subprocess.CalledProcessError:
    print("Error: Compilation failed")
    return None

  # Run the compiled executable
  try:
    result = subprocess.run(["./cpp_executable"], capture_output=True, text=True)
    return result.stdout
  except subprocess.CalledProcessError as e:
    print("Error:", e)
    return None

# Example usage:
cpp_code_file = "helloworld.cpp"
arguments = ["arg1", "arg2"]

output = run_cpp_code(cpp_code_file)

if output:
  print("C++ program output:")
  print(output)
else:
  print("An error occurred while running the C++ code.")
