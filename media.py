class Movie():
    """ The Movie Class

    This class will be used to create instances of a movie, which will be used to populate
    the fresh tomatoes website.

    Attributes:
        title (str): This is the title of the movie (e.g., Star Wars).
        art (str): This is the image url for the movie poster.
        link (str): This is a url to the movie trailer on youtube.
        overview (str): This is the summary of the movie.
        order (int): Order of the movie among other movies.
        id (int): This is the tmdb id for the movie.
        backdrop_path (string): The background image for the movie.
    """

    def __init__(self, title, art, url, overview, order, movie_id, backdrop_path):

        self.title = title
        self.poster_image_url = art
        self.trailer_youtube_url = url
        self.overview = overview
        self.order = order,
        self.movie_id = movie_id,
        self.backdrop_path = backdrop_path
