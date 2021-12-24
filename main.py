from recents_store import RecentsStore
from InquirerPy import inquirer
import argparse
import os
import webtorrentplay
from nyaa_entry import NyaaEntry
from NyaaPy import Nyaa
import smokes


def smokes_releases(args):
    # Search smokes database for animes
    # and then play the selected result
    final_result = []
    query = args.query or inquirer.text(
        "What would you like to search for?", default="").execute()
    print(f"Searching for {query}")
    smokes_json = smokes.get_json(query)
    title = smokes_json['title']
    releases = smokes.get_releases(smokes_json)
    for release_type in releases:
        print(f"{release_type}"+15*"-")
        for release in releases[release_type]:
            print(f"{title} {release} - {releases[release_type][release]}")
            nyaa_result = Nyaa.search(
                keyword=f"[{releases[release_type][release]}]{title} {release}")
            if len(nyaa_result) > 0:
                nyaa_entries = [NyaaEntry(entry['name'],
                                          entry['download_url'],
                                          entry['magnet'],
                                          entry['size'],
                                          entry['date'],
                                          entry['seeders'],
                                          entry['leechers'],
                                          entry['completed_downloads']) for entry in nyaa_result]
                nyaa_entries.sort(key=lambda x: x.get_size(), reverse=True)
                final_result.append(nyaa_entries[0])
    if len(final_result) > 0:
        chosen_entry = inquirer.select(
            message="Select a nyaa entry.",
            choices=final_result
        ).execute()
        recent_store = RecentsStore()
        recent_store.add_entry(chosen_entry)

        webtorrentplay.run(chosen_entry.get_torrent_file_url())


def run_magnet(args):
    # Plays the magnet link in mpv
    link = args.link or inquirer.text(
        message="Enter the magnet link:").execute()
    webtorrentplay.run(link)


def search_animes(args):
    # Search nyaa.si for animes
    # and then play the selected result
    # using webtorrent
    query = args.query or inquirer.text(
        message="Enter the anime name:").execute()
    print(f"Searching for {query}")
    nyaa_entries = Nyaa.search(query)
    recent_store = RecentsStore()
    torrents = [NyaaEntry(entry['name'],
                          entry['download_url'],
                          entry['magnet'],
                          entry['size'],
                          entry['date'],
                          entry['seeders'],
                          entry['leechers'],
                          entry['completed_downloads']) for entry in nyaa_entries]

    if len(nyaa_entries) > 0:
        chosen_nyaa_entry = inquirer.select(
            message="Select a nyaa entry.",
            choices=torrents[:15]
        ).execute()
        recent_store.add_entry(chosen_nyaa_entry)
        webtorrentplay.run(chosen_nyaa_entry.get_torrent_file_url())
    else:
        print("No Results Found.")


def recents_anime(args):
    # View recently watched animes
    # and then play the selected result
    recent_store = RecentsStore()
    recent_animes = recent_store.get_recents()
    if len(recent_animes) > 0:
        chosen_entry = inquirer.select(
            message="Select a recent anime.",
            choices=recent_animes
        ).execute()
        webtorrentplay.run(chosen_entry.get_torrent_file_url())
    else:
        print("No recent anime found!")


def configure_arg_parse(parser: argparse.ArgumentParser):
    sub_parsers = parser.add_subparsers()  # dest="subcommand")
    search_parser = sub_parsers.add_parser(
        "search", help="Search nyaa.si for animes.")
    search_parser.set_defaults(func=search_animes)

    search_parser.add_argument(
        "--query", "-q", dest="query", help="Search nyaa for the provided query.")

    recents_parser = sub_parsers.add_parser(
        "recents", help="View recently watched animes.")

    recents_parser.set_defaults(func=recents_anime)

    magnet_parser = sub_parsers.add_parser(
        "magnet", help="Play a magnet link.")

    magnet_parser.add_argument(
        "--link", "-l", dest="link", help="Play the provided magnet link.")

    magnet_parser.set_defaults(func=run_magnet)

    smokes_parser = sub_parsers.add_parser(
        "smokes", help="Play smokes reccomendation of anime from nyaa.si.")

    smokes_parser.add_argument(
        "--query", "-q", dest="query", help="Search smokes database for the provided query.")

    smokes_parser.set_defaults(func=smokes_releases)


def main():
    try:
        if not os.path.exists("./web_torr_dls"):
            os.makedirs("./web_torr_dls")
        parser = argparse.ArgumentParser(prog="AniWebTorr")
        configure_arg_parse(parser)
        args = parser.parse_args()
        args.func(args)
    except KeyboardInterrupt:
        pass


main()
