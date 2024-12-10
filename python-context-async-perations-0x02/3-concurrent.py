import asyncio
import aiosqlite

# Async function to fetch all users
async def async_fetch_users(database):
    """
    Fetch all users from the database asynchronously.
    """
    query = "SELECT * FROM users"
    async with aiosqlite.connect(database) as conn:
        async with conn.execute(query) as cursor:
            result = await cursor.fetchall()
            return result

# Async function to fetch users older than 40
async def async_fetch_older_users(database):
    """
    Fetch users older than 40 from the database asynchronously.
    """
    query = "SELECT * FROM users WHERE age > ?"
    params = (40,)
    async with aiosqlite.connect(database) as conn:
        async with conn.execute(query, params) as cursor:
            result = await cursor.fetchall()
            return result

# Function to perform concurrent queries
async def fetch_concurrently():
    """
    Executes async_fetch_users and async_fetch_older_users concurrently using asyncio.gather.
    """
    database = "example.db"  # SQLite database file

    # Execute both queries concurrently
    all_users_task = async_fetch_users(database)
    older_users_task = async_fetch_older_users(database)

    # Use asyncio.gather() to run the tasks concurrently
    all_users, older_users = await asyncio.gather(all_users_task, older_users_task)

    # Output the results
    print("All Users:", all_users)
    print("Users Older than 40:", older_users)

# Entry point to run the concurrent fetch
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
