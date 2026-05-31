import re

def extract_timestamps(logs: list[str]) -> list[str]:
    timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    timestamps = []
    return [re.search(timestamp_pattern, log).group() for log in logs if re.search(timestamp_pattern, log)]

def extract_errors(logs: list[str]) -> list[str]:
    error_pattern = r"ERROR"
    errors = []
    return [log for log in logs if "ERROR" in log]

def extract_ips(logs: list[str]) -> list[str]:
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    ips = []
    return [ip for log in logs for ip in re.findall(ip_pattern, log)]

def main():
    logs = [
    "2026-05-26 08:12:34 ERROR auth-service: Connection timeout (attempt 3/3)",
    "2026-05-26 08:13:01 INFO  books-service: Request completed in 142ms",
    "2026-05-26 08:13:45 ERROR db-service: Disk usage at 94% on /dev/sda1",
    "2026-05-26 08:14:02 WARN  user-service: Memory at 87%, threshold is 80%",
    "2026-05-26 08:14:55 INFO  auth-service: User login successful from 10.0.0.42",
]
    
    # Extract timestamps from the logs
    timestamps = extract_timestamps(logs)
    print("Extracted timestamps:")
    for ts in timestamps:
        print(ts)

    # Extract ERROR logs
    error_logs = extract_errors(logs)
    print("\nExtracted ERROR logs:")
    for error in error_logs:
        print(error)

    # Extract IP addresses from the logs
    ips = extract_ips(logs)
    print("\nExtracted IP addresses:")
    for ip in ips:
        print(ip)


if __name__=="__main__":
    main()