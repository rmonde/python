
def describe_server(name: str, cpu: int, memory: int, is_active: bool = True) -> str:
    return f"Server: {name} | CPU: {cpu} cores | Memory: {memory} GB | Status: {'Active' if is_active else 'Inactive'}"


def filter_servers(servers: list, active_only: bool = True) -> list:
    return [ server for server in servers if server["is_active"] == active_only ]



def main():
    server_list = [
        {"name": "Server1", "cpu": 8, "memory": 32, "is_active": True},
        {"name": "Server2", "cpu": 16, "memory": 64, "is_active": False},
        {"name": "Server3", "cpu": 4, "memory": 16, "is_active": True}
    ]

    for server in server_list:
        prefix = "[OFFLINE]" if not server["is_active"] else ""
        print(f"{prefix}{describe_server(**server)}")

    print(f"Active Servers: {filter_servers(server_list, active_only=True)}")
    print(f"Inactive Servers: {filter_servers(server_list, active_only=False)}")

if __name__ == "__main__":
    main()