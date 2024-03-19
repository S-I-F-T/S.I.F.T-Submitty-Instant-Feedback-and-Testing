import subprocess


# Compile the Java program (replace with your compilation command if needed)
subprocess.run(["javac", "hello.java"])

# Run the compiled class file
result = subprocess.run(["java", "hello.java"], capture_output=True, check=True)
print("Output from Java program (subprocess.run):")
print(result.stdout.decode())

# Example error handling (check return code)
if result.returncode != 0:
  print("Error: Java program exited with code", result.returncode)