class Anime:
    def __init__(self, title, magnet, size, seeders=None) -> None:
        self.title = title
        self.magnet = magnet
        self.size = size
        self.seeders = seeders

    def get_title(self):
        return self.title

    def get_magnet(self):
        return self.magnet

    def get_size(self):
        return self.size

    def get_seeders(self):
        return self.seeders

