import subprocess

# Define the command to execute the C shell script
# Replace 'your_script.csh' with the actual name of your C shell script
# You might need to specify the full path if the script is not in the current directory
command = ["tcsh", "your_script.csh"] 

try:
    # Execute the command
    # capture_output=True captures stdout and stderr
    # text=True decodes the output as text
    result = subprocess.run(command, capture_output=True, text=True, check=True)

    # Print the standard output and standard error
    print("STDOUT:")
    print(result.stdout)
    print("STDERR:")
    print(result.stderr)

except subprocess.CalledProcessError as e:
    # Handle errors if the script returns a non-zero exit code
    print(f"Error executing C shell script: {e}")
    print(f"STDOUT: {e.stdout}")
    print(f"STDERR: {e.stderr}")
except FileNotFoundError:
    print(f"Error: The C shell interpreter (tcsh) or the script was not found.")