import sqlite3
import functools

# Decorator to manaage ddatabase connection

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper_with_db_connection(*args, **kwargs):
        conn = sqlite3.connect('user.db')
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper_with_db_connection

# Decorator to manage transactions
def transactional(func):
    @functools.wraps(func)
    def wrapper_transactional(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            print(f"Transactional rolled back due to: {e}")
            raise
    return wrapper_transactional

# Updating user email notification
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE user SET email = ? WHERE id = ?", (new_email, user_id))

# e.g
update_user_email(user_id=1, new_email='brian.kipkemboi@gmail.com')
