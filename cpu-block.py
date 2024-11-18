import multiprocessing
import time

def stress_cpu():
    while True:
        pass 

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Starting stress test on {num_cores} cores.")
    
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=stress_cpu)
        processes.append(p)
        p.start()
    
    try:
        # Run for a specified time or until manually stopped
        time.sleep(10)
    except KeyboardInterrupt:
        print("\nStopping stress test...")
    finally:
        for p in processes:
            p.terminate()
