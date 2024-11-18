import psutil
import time

# Set the CPU usage threshold (in percentage)
THRESHOLD = 80  # Adjust this as needed

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
        
        # Wait a short time before checking again
        time.sleep(1)

if __name__ == "__main__":
    try:
        monitor_cpu(THRESHOLD)
    except KeyboardInterrupt:
        print("\nExiting monitoring script.")
