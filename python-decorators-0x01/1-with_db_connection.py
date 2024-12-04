#!/usr/bin/python3
import sqlite3
import functools

def with_db_connection():
    """
    Decorator to handle opening and closing of a database connection
    Passes the connection object to the decorateed function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('user.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    """
    Fetch a user by their ID from the database.
    """

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id))
    return cursor.fetchone()

# Fetching user by ID with Automatic connection handling
user = get_user_by_id(user_id=1)
print(user)