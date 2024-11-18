import platform
import subprocess
import os
import psutil

# Get the system name (e.g., 'Windows', 'Darwin' for macOS, 'Linux')
os_name = platform.system()

print("Operating System:", os_name)

if os_name == "Darwin": #Darwin is os_name for macOS
    print("Running on macOS")

    # Get CPU usage as a percentage of total CPU time
    cpu_percent = psutil.cpu_percent(interval=1)  # interval of 1 second to get a real-time reading

    # Get CPU usage breakdown (user, system, idle)
    cpu_percentages = psutil.cpu_percent(interval=1, percpu=False)  # Returns user, sys, idle, etc.
    

    # Get per-CPU stats (total, user, system, idle, etc.)
    print(f"CPU usage: {cpu_percent}%")
    
    cpu_times = psutil.cpu_times()  # returns namedtuple with user, system, idle, etc.

    print(f"User: {cpu_times.user}%")
    print(f"System: {cpu_times.system}%")
    print(f"Idle: {cpu_times.idle}%")
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
