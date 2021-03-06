#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import sys
import re
lib_folder = os.path.abspath('lib')
sys.path.append(lib_folder)
import entertainment_center

template_directory=os.path.join(os.path.dirname("__file__"),'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_directory))

# Entertainment center contains all the list of stored movie links and trailers
entertainmentCenter = entertainment_center.EntertainmentCenter()
# Default movies
entertainmentCenter.addMovie(
    title="Finding Nemo",
    storyline="Clownfish gets lost, his father attempts find him",
    poster="http://assets.fontsinuse.com/static/use-media-items/17/16315/full-1028x1500/56702cc2/Finding%20Nemo%20(2003)%202.jpeg?resolution=0",
    trailer="https://www.youtube.com/watch?v=wZdpNglLbt8")
entertainmentCenter.addMovie(
    title="Incredibles",
    storyline="Fantastic crime fighting family of four",
    poster="http://www.gstatic.com/tv/thumb/movieposters/35032/p35032_p_v8_aa.jpg",
    trailer="https://www.youtube.com/watch?v=fwHlyurv-0U")


def render_movie(movie):
    """
    Renders the movie properties via the movie.html template
    """
    # Extract the youtube ID from the url
    youtube_id_match = re.search(
        r'(?<=v=)[^&#]+', movie.trailer_url)
    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', movie.trailer_url)
    trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                          else None)

    # Append the tile for the movie with its content filled in
    t = jinja_env.get_template('movie.html')
    print t
    return t.render({
        "movie_title":movie.title,
        "poster_image_url":movie.poster_url,
        "trailer_youtube_id":trailer_youtube_id,
        "storyline": movie.storyline
    })

class MainHandler(webapp2.RequestHandler):
    def render_template_string(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, kw):
        self.response.out.write(self.render_template_string(template, **kw))

    def get(self):

        print [ render_movie(movie) for movie in entertainmentCenter.getMovies() ]
        self.render("index.html", {
            "movie_tiles": "".join([ render_movie(movie) for movie in entertainmentCenter.getMovies() ]),
            "prev_items": entertainmentCenter.toString()
        })

    def post(self):
        # Hidden elements to remember last ones.
        # this is a little hacky right now but hopefully databases will solve life's problems
        items = self.request.get('prev_items')
        if items:
            for itemStr in items[0].split("||"):
                itemProps = itemStr.split("|")
                print itemProps
                entertainmentCenter.addMovie(
                    itemProps[0],
                    itemProps[1],
                    itemProps[2],
                    itemProps[3])

        entertainmentCenter.addMovie(
                title=self.request.get('title'),
                storyline=self.request.get('storyline'),
                poster=self.request.get('poster'),
                trailer=self.request.get('trailer')
            )


        self.render("index.html", {
            "movie_tiles": "".join([ render_movie(movie) for movie in entertainmentCenter.getMovies() ]),
            "prev_items": entertainmentCenter.toString()
        })


app = webapp2.WSGIApplication([
    ('/', MainHandler) # you sub url + callback handler. i.e. URL Handler
], debug=True)
