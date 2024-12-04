#!/usr/bin/python3
seed = __import__('seed')

def paginate_users(page_size, offset):
    """
    Fetch paginated data from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_paginate(page_size):
    """
    Generator function to lazily load pages of data.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:
            break  # Stop iteration if no more data
        yield page
        offset += page_size
