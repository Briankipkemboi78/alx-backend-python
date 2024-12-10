#!/usr/bin/env python3

import asyncio
import aiosqlite


async def async_fetch_users():
    """
    Fetch all users from the database.
    """
    query = "SELECT * FROM users"
    async with aiosqlite.connect("example.db") as conn:
        async with conn.execute(query) as cursor:
            result = await cursor.fetchall()
            return result


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


async def fetch_concurrently():
    """
    Use asyncio.gather() to fetch all users and users older than 40 concurrently.
    """
   
    all_users, older_users = await asyncio.gather(async_fetch_users(), async_fetch_older_users())

   
    print("All Users:", all_users)
    print("Users Older than 40:", older_users)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
