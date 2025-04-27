import aiosqlite
import asyncpg

from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_TYPE


class Database:
    def __init__(self):
        self.conn = None
        self.cur = None

    async def connect(self):
        if DB_TYPE == "sqlite":
            self.conn = await aiosqlite.connect("database.db")
            self.cur = self.conn
        elif DB_TYPE == "postgres":
            self.conn = await asyncpg.create_pool(
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                host=DB_HOST,
                port=DB_PORT,
            )
        else:
            raise ValueError("Unsupported DB_TYPE")

    async def execute(self, query, *args):
        if DB_TYPE == "sqlite":
            await self.conn.execute(query, args)
            await self.conn.commit()
        elif DB_TYPE == "postgres":
            async with self.conn.acquire() as connection:
                await connection.execute(query, *args)

    async def fetchone(self, query, *args):
        if DB_TYPE == "sqlite":
            async with self.conn.execute(query, args) as cursor:
                row = await cursor.fetchone()
                return row
        elif DB_TYPE == "postgres":
            async with self.conn.acquire() as connection:
                row = await connection.fetchrow(query, *args)
                return row

    async def fetchall(self, query, *args):
        if DB_TYPE == "sqlite":
            async with self.conn.execute(query, args) as cursor:
                rows = await cursor.fetchall()
                return rows
        elif DB_TYPE == "postgres":
            async with self.conn.acquire() as connection:
                rows = await connection.fetch(query, *args)
                return rows

    async def close(self):
        if DB_TYPE == "sqlite":
            await self.conn.close()
        elif DB_TYPE == "postgres":
            await self.conn.close()

# Yagona object yaratamiz
db = Database()
