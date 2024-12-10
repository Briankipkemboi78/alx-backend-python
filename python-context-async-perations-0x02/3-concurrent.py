import asyncio
import aiosqlite

# Asynchronous function to fetch all users
async def asyncfetchusers(database):
    """
    Fetch all users from the database.
    """
    query = "SELECT * FROM users"
    async with aiosqlite.connect(database) as conn:
        async with conn.execute(query) as cursor:
            result = await cursor.fetchall()
            return result

# Asynchronous function to fetch users older than 40
async def asyncfetcholder_users(database):
    """
    Fetch users older than 40 from the database.
    """
    query = "SELECT * FROM users WHERE age > ?"
    params = (40,)
    async with aiosqlite.connect(database) as conn:
        async with conn.execute(query, params) as cursor:
            result = await cursor.fetchall()
            return result

# Asynchronous function to perform concurrent fetching
async def fetch_concurrently():
    """
    Use asyncio.gather() to fetch all users and users older than 40 concurrently.
    """
    database = "example.db"  # SQLite database file

    # Create tasks for fetching
    fetch_all_task = asyncfetchusers(database)
    fetch_older_task = asyncfetcholder_users(database)

    # Execute tasks concurrently using asyncio.gather()
    all_users, older_users = await asyncio.gather(fetch_all_task, fetch_older_task)

    # Print results
    print("All Users:", all_users)
    print("Users Older than 40:", older_users)

# Entry point to run the script
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
