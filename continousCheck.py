import platform

# Get the system name (e.g., 'Windows', 'Darwin' for macOS, 'Linux')
os_name = platform.system()

print("Operating System:", os_name)

if os_name == "Darwin":
    print("Running on macOS")
elif os_name == "Windows":
    print("Running on Windows")
elif os_name == "Linux":
    print("Running on Linux")
else:
    print("Unknown OS")
