import platform
import subprocess

# Get the system name (e.g., 'Windows', 'Darwin' for macOS, 'Linux')
os_name = platform.system()

print("Operating System:", os_name)

if os_name == "Darwin":
    print("Running on macOS")
    print("this is where the test is gonna go")
    '''
    try:
        result = subprocess.run(["bash", "/path/to/script.sh"], check=True, capture_output=True, text=True)
        print("Script Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr}")
    '''
elif os_name == "Windows":
    print("Running on Windows")
elif os_name == "Linux":
    print("Running on Linux")
else:
    print("Unknown OS")
