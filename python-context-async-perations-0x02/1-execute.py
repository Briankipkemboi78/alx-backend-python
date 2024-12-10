import mysql.connector
from mysql.connector import Error

class ExecuteQuery:
    def __init__(self, host, user, password, database, query, params=None):
        """
        Initialize the ExecuteQuery with database connection details, query, and parameters.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
        Establish the database connection, execute the query, and return the results.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor(dictionary=True)  # Use dictionary cursor for easier result access.
            self.cursor.execute(self.query, self.params)
            return self.cursor.fetchall()  # Fetch and return the query results.
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the connection and handle any exceptions if they occur.
        """
        if exc_type:
            print(f"An error occurred: {exc_value}")
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.commit()
            self.connection.close()

# Usage Example:
if __name__ == "__main__":
    # Database connection parameters
    host = "localhost"
    user = "root"
    password = "******"
    database = "alx_pro_dev"

    # Query and parameters
    query = "SELECT * FROM users WHERE age > %s"
    params = (25,)

    # Execute query using the context manager
    with ExecuteQuery(host, user, password, database, query, params) as results:
        print("Query Results:", results)