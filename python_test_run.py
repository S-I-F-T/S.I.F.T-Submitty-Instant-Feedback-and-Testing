import subprocess

# Define the path to the Python file you want to run (replace with your actual path)
script_path = "nested/subfolder/helloworld.py"

# Option 1: Using subprocess.call (simple execution)
subprocess.call([script_path])  # Pass the script path as a list

# Option 2: Using subprocess.run (more detailed information)
result = subprocess.run([script_path], capture_output=True)

# Check the return code (0 for success)
if result.returncode == 0:
    print("Script execution successful!")
else:
    print("Script execution failed. Return code:", result.returncode)

# Access standard output and error (if captured)
if result.stdout:
    print("Standard output:", result.stdout.decode())

if result.stderr:
    print("Standard error:", result.stderr.decode())