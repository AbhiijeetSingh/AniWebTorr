import os

def magnet_files(magnet):
    command=f'webtorrent download "{magnet}" -s'
    print(command)
    os.system(command)

def play_file(magnet, index):
        command=f'webtorrent download "{magnet}" -s {index} --mpv'
        print(command)
        os.system(command)

def run(magnet = None):
    if magnet == None:
        magnet = input("Enter magnet: ")
    else:
        magnet_files(magnet)
        file_index = input("Enter the file index: ")
        play_file(magnet, file_index)


