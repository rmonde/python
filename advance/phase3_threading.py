import threading
import time

def download_file(filename):
    print(f"Downloading {filename}...")
    time.sleep(2)  # Simulate time taken to download
    print(f"Done:{filename}.")
    print("-----------------------------------")

def main():
    # Create threads for each file download
    files = ["file1.txt", "file2.txt", "file3.txt"]
    # without threading
    for file in files:
        print("------------------------------------")
        start = time.time()
        download_file(file)
        elasped = time.time() - start
        print(f"Time taken to download {file}: {elasped:.2f} seconds")
        print("-----------------------------------")

    start = time.time()
    threads = []
    for filename in files:
        print("------------------------------------")
        thread = threading.Thread(target=download_file, args=(filename,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    elasped = time.time() - start
    print(f"total threaded time: {elasped:.2f}s")
    print("-----------------------------------")

if __name__ == "__main__":
    main()