class Anime:
    def __init__(self,title,magnet,size,date,seeders,leechers,completed_downloads) -> None:
        self.title = title
        self.magnet=magnet
        self.size = size
        self.date = date
        self.seeders = seeders
        self.leechers = leechers
        self.completed_downloads = completed_downloads 

    def get_title(self):
        return self.title
    
    def get_magnet(self):
        return self.magnet
    
    def get_size(self):
        return self.size
    
    def get_seeders(self):
        return self.seeders

    def get_leechers(self):
        return self.leechers
    
    def get_completed_dl(self):
        return self.completed_downloads

