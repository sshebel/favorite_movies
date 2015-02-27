import webbrowser

class Movie:
    """ Class to hold movie information for use in creating a web page of favorite movies.

        Attributes:
            name = movie name
            poster = movie poster image url
            trailer = url youtube movie trailer
            rating = movie rating, must be one of the ratings specifed in the class ratings dictionary
            year = year movie released
            category = movie category (drama, comedy, etc.)
     """       
    ratings = {'G':'<span style="color:green; font-family:Cooper Black">G</span>',
               'PG':'<span style="color:orange; font-family:Cooper Black">PG</span>',
               'PG-13':'<span style="color:purple; font-family:Cooper Black">PG-13</span>',
               'R':'<span style="color:red; font-family:Cooper Black">R</span>'}
    def __init__(self,name,poster,trailer,rating,year,category):
        self.title = name
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.rating = rating; 
        self.year = year
        self.category = category 

    def show_trailer(self):
        webbrowser.open(self.trailer)
