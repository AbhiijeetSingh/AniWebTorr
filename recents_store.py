from json.decoder import JSONDecodeError
from typing import Iterator
from nyaa_entry import NyaaEntry
import json

class RecentEntry(object):
    def __init__(self, title, magnet, size, seeders) -> None:
        self.title = title
        self.magnet = magnet
        self.size = size
        self.seeders = seeders
    
    def __repr__(self) -> str:
        return f"" 


class RecentsStore(object):
    def __init__(self) -> None:
        self.__storage_file = "./recents.json"

        
    def add_entry(self, nyaa_entry: NyaaEntry) -> None:
        assert isinstance(nyaa_entry, NyaaEntry), "Can only store NyaaEntries"
        with open(self.__storage_file, "r+") as f:
            try:
                entries = json.load(f)
            except json.decoder.JSONDecodeError:
                entries = []

        if len(entries) > 15:
            entries[0] = nyaa_entry.to_dict()
        else:
            entries.append(nyaa_entry.to_dict())

        with open(self.__storage_file, "w") as f:
            json.dump(entries, f)

    def get_recents(self) -> Iterator:
        with open(self.__storage_file, "r") as f:
            try:
                return list(map(NyaaEntry.from_dict, reversed(json.load(f))))
            except json.decoder.JSONDecodeError:
                return []

    def close(self):
        self.__file.close()

if __name__ == "__main__":
    store = RecentsStore()
    for r in store.get_recents():
        print(r)
    