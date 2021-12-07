from bs4 import BeautifulSoup
from nyaa_entry import NyaaEntry
import requests

def get_list(query):
    base_url = "https://nyaa.si/?f=0&c=0_0&q="
    query = query.strip().replace(" ", "+")
    result_page = requests.get(base_url+query)
    soup = BeautifulSoup(result_page.text, 'html.parser')
    table_data = soup.find_all("tr")
    table_data = table_data[1:]
    
    anime_mag_list=[]

    for data in table_data:
        td_list = data.find_all("td")
        links = td_list[1].find_all("a")
        
        for link in links:
            if "comment" not in link["title"]:
                title = link["title"]
        torrent_file_url = "https://nyaa.si" + td_list[2].find_all("a")[0]["href"]
        magnet = td_list[2].find_all("a")[1]["href"]
        size = td_list[3].contents[0]
        date = td_list[4].contents[0]
        seeders = td_list[5].contents[0]
        leechers = td_list[6].contents[0]
        completed_downloads = td_list[7].contents[0]
        
        anime = NyaaEntry(title=title,
                        torrent_file_url = torrent_file_url,
                        magnet=magnet,
                        size=size,
                        date=date,
                        seeders=seeders,
                        leechers=leechers,
                        completed_downloads=completed_downloads)
        
        anime_mag_list.append(anime)
    
    return anime_mag_list


