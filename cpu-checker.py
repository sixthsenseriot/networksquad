import psutil
import time
import subprocess

print(psutil.__version__)

# Set the CPU usage threshold (in percentage)
THRESHOLD = 80  # Adjust this as needed

# Function to run the continuous check script
def run_continous_check():
    try:
        subprocess.run(["python", "continousCheck.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running continuousCheck.py: {e}")

# Function to monitor CPU usage
def monitor_cpu(threshold):
    print("Monitoring CPU usage...")
    while True:
        # Get the current CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Print CPU usage
        print(f"CPU Usage: {cpu_usage}%")
        
        # Check if CPU usage exceeds the threshold
        if cpu_usage > threshold:
            print(f"ALERT: CPU usage spike detected! Usage is at {cpu_usage}%")
            run_continous_check()  # Run the continuous check script when a spike is detected
        
        # Wait a short time before checking again
        time.sleep(1)

if __name__ == "__main__":
    try:
        monitor_cpu(THRESHOLD)
    except KeyboardInterrupt:
        print("\nExiting monitoring script.")
