import requests
from bs4 import BeautifulSoup
import torrent
import asyncio
from anime import Anime

def get_list(query):
    base_url = "https://nyaa.notmarek.com/?f=0&c=0_0&q="
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
        magnet = td_list[2].find_all("a")[1]["href"]
        size = td_list[3].contents[0]
        date = td_list[4].contents[0]
        seeders = td_list[5].contents[0]
        # leechers = td_list[6].contents[0]
        # completed_downloads = td_list[7].contents[0]
        
        anime = Anime(title=title,
                        magnet=magnet,
                        size=size,
                        seeders=seeders)
        anime_mag_list.append(anime)
    
    return anime_mag_list


