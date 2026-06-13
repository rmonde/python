import multiprocessing
import time


def process_log_file(filename):
    print(f"Processing {filename}...")
    time.sleep(2)  # Simulate time taken to process
    print(f"Done: {filename}.")
    print("-----------------------------------")
    return 100  # Simulate line count


if __name__ == "__main__":
    # Create processes for each log file processing
    log_files = ["log1.txt", "log2.txt", "log3.txt", "log4.txt", "log5.txt", "log6.txt", "log7.txt", "log8.txt", "log9.txt", "log10.txt"]
    total_time_for_sequential = 0
    for file in log_files:
        print("------------------------------------")
        sequence_start = time.time()
        process_log_file(file)
        sequence_elapsed = time.time() - sequence_start
        total_time_for_sequential += sequence_elapsed
        
        print("-----------------------------------")
    
    with multiprocessing.Pool(processes=4) as pool:
        parellel_start = time.time()
        total_lines = pool.map(process_log_file, log_files)
        parellel_elapsed = time.time() - parellel_start
        print(f"Total line count: {sum(total_lines)} lines")
        
        print("-----------------------------------")


    print(f"Sequential: {total_time_for_sequential:.2f} s")
    print(f"Parallel (4 workers): {parellel_elapsed:.2f} s")