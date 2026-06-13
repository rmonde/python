class Server:
    """A class to represent a server."""

    def __init__(self, name, cpu, memory, is_active=True):
        """Initialize the server with a name, CPU, and memory."""
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self._is_active = is_active

    @property
    def status(self):
        """Getter: Return the active status of the server."""
        if self._is_active:
            return "Active"
        else:
            return "Inactive"
        
    @status.setter
    def status(self, value):
        """Setter: Set the status of the server."""
        if value.lower() == "active":
            self._is_active = True
        elif value.lower() == "inactive":
            self._is_active = False
        else:
            raise ValueError("Status must be 'Active' or 'Inactive'.")
    

    def __str__(self) -> str:
        """ Return a string representation of the server."""
        return f"Server: {self.name}, CPU: {self.cpu}, Memory: {self.memory}, Status:{ self.status } "

    def describe(self) -> str:
        """Return a description of the server."""
        return f"Server: {self.name} | CPU: {self.cpu} cores | Memory: {self.memory} GB | Status: {self.status}"

    def decommission(self):
        """Decommission the server."""
        self.status = "Inactive"
        print(f"{self.name} has been decommissioned.")

class DatabaseServer(Server):
    """A class to represent a database server, inheriting from Server."""

    def __init__(self, name, cpu, memory, is_active=True, db_type="PostgreSQL"):
        """Initialize the database server with a name, CPU, memory, and database type."""
        super().__init__(name, cpu, memory, is_active)
        self.db_type = db_type

    def __str__(self) -> str:
        """Return a string representation of the database server."""
        return f"Database Server: {self.name}, CPU: {self.cpu}, Memory: {self.memory}, DB Type: {self.db_type}, Status: {self.status} "

    def describe(self) -> str:
        """Return a description of the database server."""
        return f"{super().describe()} | DB: {self.db_type}"
    
    def backup(self):
        """Perform a backup of the database server."""
        if self.status == "Active":
            print(f"Running backup on {self.name} ({self.db_type})...")

def main():
    """The main function."""
    s1 = Server("Server1", 8, 32, True)
    s2 = Server("Server2", 16, 64, True)
    print(s1)
    print(s2)
    s1.decommission()
    print(s1)

    # Create a database server instance
    db1 = DatabaseServer("DBServer1", 16, 64, True, "MySQL")
    db2 = DatabaseServer("DBServer2", 32, 128, True, "PostgreSQL")
    print(db1.describe())
    db1.backup()
    db1.decommission()
    print()

    print(db2.describe())
    db2.backup()
    db2.decommission()
    print()

if __name__=="__main__":
    main()