import subprocess

# Define the path to the Python file you want to run (replace with your actual path)
script_path = "nested/subfolder/hw1.py"

# Option 2: Using subprocess.run (more detailed information)
result = subprocess.run(["python3", script_path], capture_output=True)

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