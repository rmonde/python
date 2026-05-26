def log_stream(lines: list):
    for line in lines:
        if "ERROR" in line:
            yield line.strip()

# paginate([1,2,3,4,5], 2) yields 
# [1,2], then [3,4], then [5]
def paginate(items: list, page_size: int):
    for i in range(0, len(items), page_size):
        yield items[i:i+page_size]

def main():
    logs = [
    "INFO: Service started",
    "ERROR: Connection timeout",
    "DEBUG: Retrying...",
    "ERROR: Disk full",
    "INFO: Service stopped"
    ]

    for line in log_stream(logs):
        print(line)

    for page in paginate([1,2,3,4,5], 2):
        print(page)

if __name__=="__main__":
    main()