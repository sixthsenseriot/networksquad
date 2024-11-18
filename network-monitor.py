import psutil
import socket
import time
from datetime import datetime

# Function to get network interface details
def get_network_config():
    print("Network Configuration:")
    # Get network interfaces (ip addresses, mac addresses, etc.)
    addrs = psutil.net_if_addrs()
    for interface, addr_list in addrs.items():
        print(f"\nInterface: {interface}")
        for addr in addr_list:
            print(f"  Address: {addr.address}")
            if addr.family == socket.AF_INET:
                print(f"    IPv4 Address: {addr.address}")
            elif addr.family == socket.AF_INET6:
                print(f"    IPv6 Address: {addr.address}")
            elif addr.family == psutil.AF_LINK:
                print(f"    MAC Address: {addr.address}")

# Function to monitor network utilization (bytes sent and received)
def monitor_network_utilization(interval=1):
    print("\nMonitoring Network Utilization:")
    last_recv, last_sent = psutil.net_io_counters().bytes_recv, psutil.net_io_counters().bytes_sent
    
    while True:
        # Get current bytes sent and received
        net_io = psutil.net_io_counters()
        bytes_recv = net_io.bytes_recv
        bytes_sent = net_io.bytes_sent

        # Calculate utilization since last check
        recv_diff = bytes_recv - last_recv
        sent_diff = bytes_sent - last_sent

        print(f"\n{datetime.now()} - Network Utilization:")
        print(f"  Bytes Received: {recv_diff} bytes")
        print(f"  Bytes Sent: {sent_diff} bytes")
        print(f"  Total Received: {bytes_recv} bytes")
        print(f"  Total Sent: {bytes_sent} bytes")

        # Update previous values for the next calculation
        last_recv, last_sent = bytes_recv, bytes_sent
        
        # Wait for the next iteration (default is 1 second)
        time.sleep(interval)

if __name__ == "__main__":
    # Print network configuration
    get_network_config()
    
    # Start monitoring network utilization (default every 1 second)
    monitor_network_utilization()
