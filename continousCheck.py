import psutil
import time

# Wait for an interval to accurately measure CPU usage
time.sleep(1)  # This ensures that the first call does not return 0.0%

# Get CPU usage for each core
cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)

# Print CPU utilization for each core
for i, usage in enumerate(cpu_per_core):
    print(f"Core {i}: {usage}%")

