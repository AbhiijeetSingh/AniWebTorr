from recents_store import RecentsStore
import nyaa
import torrent
from InquirerPy import inquirer
import argparse
import os

def search_animes(args):
    query = args.query or inquirer.text(message = "Enter the anime name:").execute()
    nyaa_entries = nyaa.get_list(query)
    recent_store = RecentsStore()
    
    if len(nyaa_entries) > 0:
        chosen_nyaa_entry = inquirer.select(
            message = "Select a nyaa entry.",
            choices = nyaa_entries[:15]
        ).execute()
        recent_store.add_entry(chosen_nyaa_entry)
        torrent.run(chosen_nyaa_entry.get_torrent_file_url())
    else:
        print("No Results Found.")

def recents_anime(args):
    recent_store = RecentsStore()
    recent_animes = recent_store.get_recents()
    if len(recent_animes) > 0:
        chosen_entry = inquirer.select(
            message = "Select a recent anime.",
            choices = recent_animes
        ).execute()
        torrent.run(chosen_entry.get_torrent_file_url())
    else:
        print("No recent anime found!")

def a(b):
    print(b)

def configure_arg_parse(parser: argparse.ArgumentParser):
    sub_parsers = parser.add_subparsers()#dest="subcommand")
    search_parser = sub_parsers.add_parser("search", help="Search nyaa.si for animes.")
    search_parser.set_defaults(func=search_animes)
    # search_parser.set_defaults(func=a)
    search_parser.add_argument("--query", "-q", dest="query", help="Search nyaa for the provided query.")
    recents_parser = sub_parsers.add_parser("recents", help="View recently watched animes.")
    recents_parser.set_defaults(func=recents_anime)

def main():
    try:
        if not os.path.exists("./web_torr_dls"):
            os.makedirs("./web_torr_dls")
        parser = argparse.ArgumentParser(prog = "AniWebTorr")
        configure_arg_parse(parser)
        args = parser.parse_args()
        args.func(args)
    except KeyboardInterrupt:
        pass    
    
main()