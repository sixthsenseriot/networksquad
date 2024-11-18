import psutil
import time

# Wait for an interval to accurately measure CPU usage
time.sleep(1)  # This ensures that the first call does not return 0.0%

# Get CPU usage for each core
cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)

# Print CPU utilization for each core
for i, usage in enumerate(cpu_per_core):
    print(f"Core {i}: {usage}%")

# Allow time for accurate CPU percentage measurement
time.sleep(1)

# Initialize variables to track the process with the highest CPU utilization
highest_cpu_proc = None
highest_cpu_usage = 0.0

# Iterate over all running processes
for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
    try:
        # Check the current CPU utilization of the process
        cpu_usage = proc.info['cpu_percent']

        # Update the highest CPU process if the current one uses more CPU
        if cpu_usage != None:    
            if cpu_usage > highest_cpu_usage:
                highest_cpu_proc = proc
                highest_cpu_usage = cpu_usage

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass  # Ignore processes that can't be accessed or no longer exist

# Print the process with the highest CPU utilization
if highest_cpu_proc:
    print(f"Process with the highest CPU usage:")
    print(f"PID: {highest_cpu_proc.info['pid']}")
    print(f"Name: {highest_cpu_proc.info['name']}")
    print(f"CPU Usage: {highest_cpu_usage}%")
else:
    print("No process found with significant CPU usage.")