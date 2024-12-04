#!/usr/bin/python3
seed = __import__('seed')

def stream_user_ages():
    """ 
    Generator that yields user ages one by one
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")

    for row in cursor:
        yield row['age']

    connection.close()

def calculate_average_age():
    """
    Calculate average age of users using the stream_user_ages_generator.
    """

    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    if count == 0:
        print("Average age of users: N/A (no data)")
    else:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")