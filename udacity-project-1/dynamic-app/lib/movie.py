# Movie class
# @author: Himadri Kakran
import webbrowser
class Movie:
    """
    This is my movie class which outlines certain proeprties of a movie.
    """

    # CLASS VARIABLES (STATICS)
    VALID_RAITINGS = ["G", "PG", "PG-13", "R", "NR"]

    # CONSTRUCTOR
    def __init__(self, title, storyline, poster, trailer):
        assert isinstance(title, basestring)
        assert isinstance(storyline, basestring)
        assert isinstance(poster, basestring)
        assert isinstance(trailer, basestring)
        #Movie title
        self.title = title
        #Movie trailer link
        self.trailer_url = trailer
        #Movie storyline
        self.storyline = storyline
        #Movie poster image
        self.poster_url = poster

    # PUBLIC METHODS
    def showTrailer(self):
        """Opens web browser and plays toy story url
        """
        webbrowser.open(self.trailer_url)

    def toString(self):
        return self.title+"|"+self.storyline+"|"+self.poster_url+"|"+self.trailer_url
