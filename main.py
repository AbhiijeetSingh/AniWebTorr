from recents_store import RecentsStore
import nyaa
import torrent
from InquirerPy import inquirer

def configure_arg_parse(parser):
    pass

def main():
    
    query = input("Enter the anime name: ")
    nyaa_entries = nyaa.get_list(query)
    recent_store = RecentsStore()
    if len(nyaa_entries) > 0:
        chosen_nyaa_entry = inquirer.select(
            message = "Select a nyaa entry",
            choices = nyaa_entries[:15]
        ).execute()
        recent_store.add_entry(chosen_nyaa_entry)
    else:
        print("No Results Found")
    
    print(recent_store.get_recents())
main()