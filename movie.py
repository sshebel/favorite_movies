import webbrowser

class Movie:

    ratings = {'G':'<span style="color:green; font-family:Cooper Black">G</span>',
               'PG':'<span style="color:orange; font-family:Cooper Black">PG</span>',
               'PG-13':'<span style="color:purple; font-family:Cooper Black">PG-13</span>',
               'R':'<span style="color:red; font-family:Cooper Black">R</span>'}
    def __init__(self,name,poster,trailer,rating,year,category):
        self.title = name
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.rating = rating; # must be one of the ratings in the ratings dictionary
        self.year = year
        self.category = category # Drama, Comedy, etc.

    def show_trailer(self):
        webbrowser.open(self.trailer)
