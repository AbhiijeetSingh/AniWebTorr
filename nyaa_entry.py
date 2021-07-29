class NyaaEntry:
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

    def __repr__(self):
        title = self.title if len(self.title) < 50 else f"{self.title[:47]}..."
        return f"|{title:60s}|{self.size:^8s}|{self.seeders:^5s}|"

    def __str__(self):
        return repr(self)
    
    def to_dict(self):
        return {
        "title" : self.title,
        "magnet" : self.magnet,
        "size" : self.size,
        "date" : self.date,
        "seeders" : self.seeders,
        "leechers" : self.leechers, 
        "completed_downloads" : self.completed_downloads 
        }

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
        title = data_dict["title"],
        magnet = data_dict["magnet"],
        size = data_dict["size"],
        date = data_dict["date"],
        seeders = data_dict["seeders"],
        leechers = data_dict["leechers"],
        completed_downloads = data_dict["completed_downloads"]
        )