import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    def __init__(self, host, user, password, database):
        """
        Initializing the databaseconnection with the parameters
        """

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None


    def __enter__(self):
        """
        Database connection and return the cursor
        """
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
                
            )
            self.cursor = self.connection.cursor(dictionary=True)
            return self.cursor
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the connection and handle any exception that occurred in the block
        """
        if exc_type:
            print(f"An error occurred: {exc_value}")
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.commit()
            self.connection.close()
            
    
if __name__ == "__main__":
    # MySQL database connection parameters
    host = "localhost"
    user = "root"
    password = "*******"
    database = "alx_pro_dev"

    # Use the context manager to query the database
    with DatabaseConnection(host, user, password, database) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        print("Query Results:", results)

