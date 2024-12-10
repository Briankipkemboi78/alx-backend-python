import aiosqlite
import asyncio

# Asynchronous function to fetch all users
async def async_fetch_users(db_name):
    """
    Fetch all users from the database asynchronously.
    """
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            return users

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users(db_name):
    """
    Fetch users older than 40 from the database asynchronously.
    """
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            older_users = await cursor.fetchall()
            return older_users

# Function to execute both queries concurrently
async def fetch_concurrently():
    """
    Execute both queries concurrently using asyncio.gather.
    """
    db_name = "example.db"  # SQLite database name
    tasks = [
        async_fetch_users(db_name),
        async_fetch_older_users(db_name)
    ]
    results = await asyncio.gather(*tasks)  # Run tasks concurrently
    all_users, older_users = results
    print("All Users:", all_users)
    print("Users Older than 40:", older_users)

# Entry point to run the concurrent fetch
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
