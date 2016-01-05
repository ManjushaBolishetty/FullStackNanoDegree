#import the python module to help connect to the webbrowser
import webbrowser

#Defining class Movie
class Movie():
    """This class provides a way to store movie related information"""
    #Constructor that initializes the members of class movie.
    def __init__(self, movie_title,movie_storyline, poster_image,trailer_youtube,MPAARating, IMDbDetails,year_released):
        #assigning values to the members of class movie
        self.title = movie_title
        self.movieStoryline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.MPAA_rating = MPAARating
        self.IMDb_details = IMDbDetails
        self.Year_Released = year_released

    #Show trailer function that displays or plays the trailers of the movie.
    def show_trailer(self):
        #module.function(argument) - open function to open the trailer of the movie
        webbrowser.open(self.trailer_youtube_url)
