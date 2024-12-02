#!/usr/bin/python3
# Import necessary functions from seed.py
import seed

def main():
    # Step 1: Connect to MySQL server
    connection = seed.connect_db()
    if not connection:
        print("Failed to connect to MySQL server.")
        return

    # Step 2: Create the ALX_prodev database if it doesn't exist
    seed.create_database(connection)
    connection.close()

    # Step 3: Connect to the ALX_prodev database
    connection = seed.connect_to_prodev()
    if not connection:
        print("Failed to connect to the ALX_prodev database.")
        return

    # Step 4: Create the user_data table
    seed.create_table(connection)

    # Step 5: Insert data from the CSV file
    data_file = 'user_data.csv'  # Ensure this file exists in the same directory
    seed.insert_data(connection, data_file)

    # Step 6: Perform some checks
    cursor = connection.cursor()

    # Verify database creation
    cursor.execute(
        "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'ALX_prodev';"
    )
    if cursor.fetchone():
        print("Database ALX_prodev is present.")

    # Fetch and display a few rows from the user_data table
    cursor.execute("SELECT * FROM user_data LIMIT 5;")
    rows = cursor.fetchall()
    print("Sample data from user_data table:")
    for row in rows:
        print(row)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
