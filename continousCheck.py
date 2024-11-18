import subprocess
import os
import platform
import psutil

# Get the system name (e.g., 'Darwin' for macOS, 'Windows', 'Linux')
os_name = platform.system()

print("Operating System:", os_name)

if os_name == "Darwin":  # Darwin is the name for macOS
    print("Running on macOS")

    # Get the CPU usage as a percentage of total CPU time (this includes all states: user, system, idle, etc.)
    cpu_percent = psutil.cpu_percent(interval=1)  # interval of 1 second to get a real-time reading

    # Get the CPU usage breakdown as percentages (user, system, idle, etc.)
    cpu_times_percent = psutil.cpu_times_percent(interval=1)  # This gives percentages, not absolute times

    print(f"Total CPU Usage: {cpu_percent}%")
    print(f"User CPU Usage: {cpu_times_percent.user}%")
    print(f"System CPU Usage: {cpu_times_percent.system}%")
    print(f"Idle CPU Usage: {cpu_times_percent.idle}%")

elif os_name == "Windows":
    print("Running on Windows")
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_times_percent = psutil.cpu_times_percent(interval=1)
    print(f"CPU usage: {cpu_percent}%")
    print(f"User: {cpu_times_percent.user}%")
    print(f"System: {cpu_times_percent.system}%")
    print(f"Idle: {cpu_times_percent.idle}%")
    
elif os_name == "Linux":
    print("Running on Linux")
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_times_percent = psutil.cpu_times_percent(interval=1)
    print(f"CPU usage: {cpu_percent}%")
    print(f"User: {cpu_times_percent.user}%")
    print(f"System: {cpu_times_percent.system}%")
    print(f"Idle: {cpu_times_percent.idle}%")
    
else:
    print("Unknown OS")





