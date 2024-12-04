import mysql.connector

def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="your_user",  # Replace with your MySQL username
            password="your_password",  # Replace with your MySQL password
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def stream_users_in_batches(batch_size):
    """
    Generator to fetch data in batches from the database.
    Args:
        batch_size (int): The number of rows to fetch in each batch.
    Yields:
        List[dict]: List of user rows in the current batch.
    """
    connection = connect_to_prodev()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM user_data"
        cursor.execute(query)
        
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
        
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    """
    Process each batch to filter users over the age of 25.
    Args:
        batch_size (int): The number of rows to process in each batch.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
