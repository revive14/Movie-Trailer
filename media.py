import webbrowser

class Movie():
    """
    Movie class contains movies information

    Attributes:
    title (str): contains the movie title
    storyline (str): contains a small description of what movie is about
    poster_image_url (str): contains the movies poster image url
    trailer_youtube_url (str): contains the movie trailer on youtube

    """
    def __init__(self,title, movie_storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        return webbrowser.open(self.trailer_youtube_url)
