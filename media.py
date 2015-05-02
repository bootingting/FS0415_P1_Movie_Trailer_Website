import webbrowser

class Movie():
   
    # Movie is a class used to store a movie's year, title, poster URL, YouTube trailer link and main movie stars
    # _init_ initializes the variables in the class
    def __init__(self, movie_year, movie_title, movie_storyline, poster_image, trailer_youtube, movie_stars):
        self.year = movie_year     
        self.title = movie_title
        self.storyline = "Synopsis : " + movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.stars = "Starring : " + movie_stars

    # show trailer opens the movie trailer in a separate webbrowser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

