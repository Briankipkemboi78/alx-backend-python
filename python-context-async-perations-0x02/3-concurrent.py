import asyncio
import aiomysql

# Asynchronous function to fetch all users
async def async_fetch_users(host, user, password, database):
    """
    Fetch all users from the MySQL database asynchronously.
    """
    async with aiomysql.connect(
        host=host, user=user, password=password, db=database
    ) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM users")
            users = await cur.fetchall()
            return users

# Asynchronous function to fetch users older than 40
async def async_fetch_older_users(host, user, password, database):
    """
    Fetch users older than 40 from the MySQL database asynchronously.
    """
    async with aiomysql.connect(
        host=host, user=user, password=password, db=database
    ) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM users WHERE age > 40")
            older_users = await cur.fetchall()
            return older_users

# Function to execute both queries concurrently
async def fetch_concurrently():
    """
    Execute both queries concurrently using asyncio.gather.
    """
    # MySQL connection details
    host = "localhost"
    user = "root"
    password = "*******"
    database = "alx_pro_dev"

    # Create tasks for concurrent execution
    tasks = [
        async_fetch_users(host, user, password, database),
        async_fetch_older_users(host, user, password, database)
    ]

    results = await asyncio.gather(*tasks)  # Run tasks concurrently
    all_users, older_users = results

    print("All Users:", all_users)
    print("Users Older than 40:", older_users)

# Entry point to run the concurrent fetch
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
