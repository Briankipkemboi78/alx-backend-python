
import mysql.connector
import csv
import uuid

def connect_db():
    """
    Connects to the MySQL database server.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Change this based on MySQL configuration
            password='XXXXX',  # Change this based on MySQL configuration
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    """
    Creating the database ALX_prodev if it doesn't exist.
    """
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    connection.commit()
    cursor.close()
    print("Database ALX_prodev created successfully or already exists.")

def connect_to_prodev():
    """
    Connecting to the database in MySQL.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='(Sivan@63537891)',  
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    """
    Creates the user_data table if it doesn't exist.
    """
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data (
        user_id UUID PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(5, 2) NOT NULL
    )
    """)
    connection.commit()
    print("Table user_data created successfully or already exists.")
    cursor.close()

def insert_data(connection, csv_file):
    """
    Inserts data from a CSV file into the user_data table.
    """
    cursor = connection.cursor()
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if present
        for row in reader:
            user_id = str(uuid.uuid4())  
            name, email, age = row[0], row[1], row[2]
            cursor.execute("""
            INSERT INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE user_id=user_id
            """, (user_id, name, email, age))
    connection.commit()
    print(f"Data from {csv_file} inserted successfully.")
    cursor.close()

def stream_rows(connection):
    """
    A generator function that streams rows from the user_data table one by one.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()

