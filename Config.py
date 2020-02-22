
class Config:
    def __init__(self):

        protocol = 'http://'
        domain = 'localhost:'
        port = '8080'
        path = '/app/videogames'
        self.url = protocol+domain+port+path

    def get_url(self):
       return self.url