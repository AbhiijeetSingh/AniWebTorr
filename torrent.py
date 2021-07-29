import os
import shutil
from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator

def delete_downloaded_files():
    if os.path.isdir("web_torr_dls"):
        shutil.rmtree("web_torr_dls")

def print_torrent_files(torrent_id):
    command=f'webtorrent download "{torrent_id}" -s'
    os.system(command)

def play_file(torrent_id, index):
    command=f'webtorrent download "{torrent_id}" -s {index} -o ./web_torr_dls --mpv'
    os.system(command)

def run(torrent_id = None):
    print_torrent_files(torrent_id)
    file_index = inquirer.text(
        message = "Enter the index of the file to be played.",
        validate = NumberValidator()
        ).execute()
    play_file(torrent_id, file_index)
    delete_downloaded_files()