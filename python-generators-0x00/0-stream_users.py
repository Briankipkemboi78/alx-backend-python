import mysql.connector
import seed  # Importing the seed file for the database setup

def stream_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    for row in cursor:
        yield row
    cursor.close()

if __name__ == "__main__":
    connection = seed.connect_to_prodev()

    if connection:
        # Using the generator to stream data
        for row in stream_data(connection):
            print(row)

        connection.close()
