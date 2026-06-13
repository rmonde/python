def create_report(*metrics):
    for i, metric in enumerate(metrics, start=1):
        print(f"{i}. {metric}")

def log_event(level, message, **context):
    print(f"[{level.upper()}] {message}", end="")
    for key, value in context.items():
        print(f" | {key}={value}", end="")
    print()  # Print a newline at the end

def main():
    metrics_data = ["CPU Usage", "Memory Usage", "Disk I/O", "Network Throughput"]

    create_report(*metrics_data)

    system_events = {
        "level": "info",
        "message": "Deployment started",
        "env": "prod",
        "region": "eastus"
    }

    log_event(**system_events)

    system_events = {
        "level": "warning",
        "message": "Health check skipped"
    }

    log_event(**system_events)

if __name__ == "__main__":
    main()