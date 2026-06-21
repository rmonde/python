

def main():
    services = [
    {"name": "auth-service",  "replicas": 2, "healthy": True},
    {"name": "books-service", "replicas": 0, "healthy": False},
    {"name": "user-service",  "replicas": 3, "healthy": True},
    {"name": "db-service",    "replicas": 1, "healthy": True},
]
    # Filter out healthy services
    health_services = list(filter(lambda s: s["healthy"], services))
    print("Healthy services:")
    for service in health_services:
        print(f"{service}")

    # Sort all services by replicas in descending order
    sorted_services = sorted(services, key=lambda s:s["replicas"], reverse=True)
    print("\nServices sorted by replicas (descending):")
    for service in sorted_services:
        print(f"{service}")

    # Build a new dictionary with service name and replicas
    service_replicas = {s["name"]: s["replicas"] for s in services}
    print("\nService replicas:")
    for service in service_replicas:
        print(f"{service}: {service_replicas[service]}")
    
    # Build new list with services name with replica count as 0
    service_replicas_zero = [s["name"] for s in services if s["replicas"] == 0]
    print("\nServices with 0 replicas:")
    print(f"{service_replicas_zero}")

if __name__ == "__main__":
    main()