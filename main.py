import nyaa
import torrent
import asyncio
from tabulate import tabulate

async def main():
    
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

    print(f"{selected_title} {selected_magnet} {selected_size} {selected_seeders}")

    await torrent.run(magnet=selected_magnet)

asyncio.run(main())