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
import movie

class EntertainmentCenter:
    """
    Holds all the movies
    """
    def __init__(self, items=None):
        if items:
            assert isinstance(items, list)
            self.items = items
        else:
            self.items = list()

    def getMovies(self):
        return self.items

    def addMovie(self, title, storyline, poster, trailer):
        """
        Adds a movie to this entertainment center
        """
        m = movie.Movie(trailer=trailer,
            title=title,
            storyline=storyline,
            poster=poster)
        self.items.append(m)

    def addTv(self, properties):
        # todo
        print "Coming soon"

    def toString(self):
        content = ''
        for item in self.items:
            content += "||"+item.toString()

        return content