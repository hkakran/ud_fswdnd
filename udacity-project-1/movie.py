# Movie class
# @author: Himadri Kakran
import webbrowser
import jinja2
import re
import os

template_directory=os.path.join(os.path.dirname("__file__"),'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_directory))

class Movie:
    """
    This is my movie class which outlines certain proeprties of a movie.
    It can launch movie trailers on a web browser also
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

    def render(self):
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', self.trailer_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', self.trailer_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        t = jinja_env.get_template('movie_tile.html')
        return t.render({
            "movie_title":self.title,
            "poster_image_url":self.poster_url,
            "trailer_youtube_id":trailer_youtube_id,
            "storyline": self.storyline
        })
