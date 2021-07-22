import os
from concurrent.futures import ThreadPoolExecutor
import asyncio


async def magnet_files(magnet):
    with ThreadPoolExecutor(1) as pool:
        loop = asyncio.get_event_loop()
        command=f'webtorrent download "{magnet}" -s'
        print(command)
        info = await loop.run_in_executor(pool, os.system,
                                   command
                                   )

async def play_file(magnet, index):
    with ThreadPoolExecutor(1) as pool:
        loop = asyncio.get_event_loop()
        command=f'webtorrent download "{magnet}" -s {index} --mpv'
        print(command)
        info = await loop.run_in_executor(pool, os.system,
                                   command
                                   )

async def run(magnet = None):
    if magnet == None:
        magnet = input("Enter magnet: ")
    else:
        await magnet_files(magnet)
        file_index = input("Enter the file index: ")
        await play_file(magnet, file_index)

#asyncio.run(run())

