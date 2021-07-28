from sqlalchemy.sql.expression import table
import nyaa
import torrent
import asyncio
from tabulate import tabulate
import recents
from databases import Database


async def anime_from_nyaa(recents_database):
    query = input("Enter the anime name: ")
    query = query.replace(" ", "+")

    anime_mag_list = nyaa.get_list(query)

    table = [["Index", "Title", "Size", "Seeders"]]

    for index in range(len(anime_mag_list)):
        title = anime_mag_list[index].get_title()[:50]+"..."
        size = anime_mag_list[index].get_size()
        seeders = anime_mag_list[index].get_seeders()
        table.append([index, title, size, seeders])

    print(tabulate(table,))

    selected_index = int(input("\nEnter index: "))
    selected_title = anime_mag_list[selected_index].get_title()
    selected_magnet = anime_mag_list[selected_index].get_magnet()
    selected_size = anime_mag_list[selected_index].get_size()
    selected_seeders = anime_mag_list[selected_index].get_seeders()
    await recents.insert_data(recents_database,
                              selected_title,
                              selected_magnet,
                              selected_size,
                              selected_seeders)

    print(selected_title)
    await torrent.run(magnet=selected_magnet)


async def anime_from_magnet():
    magnet = input("Enter magnet: ")
    torrent.run()
    await torrent.run(magnet=magnet)


async def recents_table(recents_database):
    values = await recents.get_values(recents_database)
    recents_table = [["Index", "Title", "Size", "Seeders"]]
    values.reverse()
    show_length = 10 if len(values) > 10 else len(values)
    for index in range(show_length):
        value = values[index]
        row = [index, value[0], value[2], value[3]]
        recents_table.append(row)
    print(tabulate(recents_table))


async def play_from_recents(recents_database, index):
    # print("\nRecents:\n")
    values = await recents.get_values(recents_database)
    values.reverse()
    await torrent.run(values[index][1])


async def main():
    recents_database = await recents.get_database()
    await recents_table(recents_database)
    print("""
    N. Anime From Nyaa.
    M. Anime From Unique Magnet.
    Q. Quit
    """)
    option = input("Enter Option: ")
    if option.isalpha():
        if option == "N":
            await anime_from_nyaa(recents_database)
        elif option == "M":
            await anime_from_magnet()
        elif option == "Q":
            await recents_database.disconnect()
            exit()
    elif option.isdigit():
        option = int(option)
        await play_from_recents(recents_database, option)
    await recents_database.disconnect()


asyncio.run(main())
