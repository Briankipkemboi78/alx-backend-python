import time
import sqlite3
import functools

# Global dictioanry to store query results
query_cache = {}

def with_db_connection(func):
    """
    Decorator to provide a database connection to the decorated function
    """
    @functools.wraps(func)
    def wrapper_with_connection(*args, **Kwargs):
        conn = sqlite3.connect("user.db")
        try:
            # Creating a sample table and inserting data 
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOE EXISTS users (id INTEGER PRIMARY KEY, email TEXT)")
            cursor.execute("INSERT INTO users (id, email) VALUES (1, 'briankipk@gmail.com')")
            cursor.execute("INSERT INTO users (id, email) VALUES (2, 'briankipkemboi@gmail.com')")
            conn.commit()
        
            result = func(conn, *args, **Kwargs)  # passing the connection to the decorated function
        finally:
            conn.close()
        return result
    return wrapper_with_connection

def cache_query(func):
    """
    Decorator to cache the results of a database query
    """
    @functools.wraps(func)
    def wrapper_cache_query(conn, query, *args, **kwargs):
        # Check to find out if the query results is already cached
        if query in query_cache:
            print("Using cached result for query:", query)
            return query_cache[query]
        
        # Execute the query and cache the result
        print("Executing query and caching results:", query)
        result = func(conn, query, *args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper_cache_query

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """
    Fetch users from the database using the given query
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# This will fir cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)