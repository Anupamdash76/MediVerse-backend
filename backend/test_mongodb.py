import asyncio

from app.database.mongodb import db


async def main():
    collections = await db.list_collection_names()
    print(collections)


asyncio.run(main())