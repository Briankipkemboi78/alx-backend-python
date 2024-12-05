import time
import sqlite3
import functools

# Connection with db
def with_db_connection(func):
    """
    A decorator to provide a database connection.
    The connection is passed as the first argument to the decorated function
    """
    @functools.wraps(func)
    def wrapper_with_db_Connection(*args, **kwargs):
        conn = sqlite3.connect("user.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper_with_db_Connection

# Implementing retry on error
def retry_on_failure(retries=3, delay=2):
    """
    A decorator that retries the decorated function if it raises an exception.
    :param retries: Number of retries
    :param delay: Delay between retries in seconds
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper_retry_on_failure(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(conn, *args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                raise last_exception
            return wrapper_retry_on_failure
        return decorator
    
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """
    Fetches users from the database
    """
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    cursor.execute("INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com')")
    cursor.execute("INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane.smith@example.com')")
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Attempt to fetch users with automatic retry on failure
try:
    users = fetch_users_with_retry()
    print(users)
except Exception as e:
    print(f"Operation failed after retries: {e}")