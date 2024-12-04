#!/usr/bin/python3
import sqlite3
import functools
from datetime import datetime

def log_queries():
    """
    Decorators to log SQL queries before executing them
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            query = kwargs.get('query', args[0] if args else none)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if query:
                print(f"[{timestamp}] Executing SQL Query: {query}")
            else:
                print(f"[{timestamp}] Executing SQL Query: (No Query Found)")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log_queries
def fetch_all_users(query):
    """
    Fetch all users from the database
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Fetching users while logging the query 
users = fetch_all_users(query="SELECT * FROM users")
print(users)