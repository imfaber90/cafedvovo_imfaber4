from databases import Database as db
import asyncio

database = db('sqlite+aiosqlite:///cafevovo.db')

async def delete():
    await database.connect()

    query = """DROP TABLE sqlite_sequence"""
    await database.execute(query=query)

asyncio.run(delete())