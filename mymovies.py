from movie import Movie
import fresh_tomatoes

# Create an html page containing information about my favorite movies and access to the trailers.
# Create a Movie class instance for each movie to be displayed
knights_tale=Movie("A Knight's Tale",
                         "http://upload.wikimedia.org/wikipedia/en/a/a6/AKnightsTale.jpg",
                         "https://www.youtube.com/watch?v=KXvp57cURpU","PG-13","2001","Drama/Action")

sound_of_music=Movie("The Sound of Music",
               "https://www.movieguide.org/wp-content/uploads/2012/08/The-Sound-of-Music-movie-poster1.jpg",
               "https:www.youtube.com/watch?v=TRPEpJHI9zg","G","1965","Drama/Romance")

gladiator=Movie("Gladiator",
                "http://posterpress.us/uploads/g/gladiator_2000.jpg",
                "www.youtube.com/watch?v=IvTT29cavKo","R","2000","Drama/Action")

# create list of movies to pass to open_movies_page function
movies=[gladiator,knights_tale, sound_of_music]

# create the web page
fresh_tomatoes.open_movies_page(movies)
