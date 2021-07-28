
from databases import Database
import asyncio
import os


async def insert_data(database, i_title, i_magnet, i_size, i_seeders):
    query = f"INSERT INTO AnimeRecents VALUES ('{i_title}', '{i_magnet}', '{i_size}', '{i_seeders}');"
    await database.execute(query=query)


async def initiate_database():
    database = Database('sqlite:///recents.db')
    await database.connect()
    create_anime_recents_table = """CREATE TABLE AnimeRecents (title text,magnet text,size text, seeders text)"""
    await database.execute(query=create_anime_recents_table)
    return database


async def get_values(database):
    query = "SELECT * FROM AnimeRecents"
    rows = await database.fetch_all(query=query)
    #print('AnimeRecents', rows)
    return rows


async def get_database():
    if not os.path.exists("recents.db"):
        database = await initiate_database()
    else:
        database = Database('sqlite:///recents.db')
        await database.connect()
    return database

if __name__ == "__main__":
    database = asyncio.run(get_database())
    print(asyncio.run(get_values(database)))
