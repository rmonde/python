# This code is written to depict asynchronous programming using asyncio in Python. It demonstrates how to run multiple tasks concurrently without blocking the main thread.
import asyncio
import time

async def download_file(file_name):
    print(f"Starting to download {file_name}...")
    await asyncio.sleep(2)  # Simulating a time-consuming download operation
    print(f"Finished downloading {file_name}.")


async def main():
    files = ["file_0.txt", "file_1.txt", "file_2.txt", "file_3.txt", "file_4.txt"]  # List of files to download
    tasks = [download_file(file) for file in files]  # Creating a list of tasks
    await asyncio.gather(*tasks)  # Running all tasks concurrently

if __name__ == "__main__":
    start_time = time.time()
    print(f"Start time: {time.ctime(start_time)}")
    asyncio.run(main())  # Running the main function which executes the tasks
    end_time = time.time()
    print(f"End time: {time.ctime(end_time)}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")