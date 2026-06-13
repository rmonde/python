import threading
import time

# Shared list variable
shared_list = []
shared_counter = 0
lock = threading.Lock()

def write_entry(thread_counter):
    global shared_counter
    for i in range(0,5):
        shared_list.append(f"[Thread-{thread_counter}] Entry-{i}")
        with lock:
            current = shared_counter
            time.sleep(0)
            shared_counter = current + 1

        

def main():
    threads = []

    for i in range (1,11):
        thread = threading.Thread(target=write_entry, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Total entries (list): {len(shared_list)}")
    print(f"Total entries (counter): {shared_counter}")

if __name__ == "__main__":
    main()