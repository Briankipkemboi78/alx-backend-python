import asyncio
import aiosqlite

# Asynchronous function to fetch all users
async def async_fetch_users():
    """
    Fetch all users from the database.
    """
    query = "SELECT * FROM users"
    async with aiosqlite.connect("example.db") as conn:
        async with conn.execute(query) as cursor:
            result = await cursor.fetchall()
            return result

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users():
    """
    Fetch users older than 40 from the database.
    """
    query = "SELECT * FROM users WHERE age > ?"
    params = (40,)
    async with aiosqlite.connect("example.db") as conn:
        async with conn.execute(query, params) as cursor:
            result = await cursor.fetchall()
            return result

# Asynchronous function to run both queries concurrently
async def fetch_concurrently():
    """
    Use asyncio.gather() to fetch all users and users older than 40 concurrently.
    """
    # Use asyncio.gather() to execute both queries concurrently
    all_users, older_users = await asyncio.gather(async_fetch_users(), async_fetch_older_users())

    # Print results
    print("All Users:", all_users)
    print("Users Older than 40:", older_users)

# Entry point to run the script
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
