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

template_directory=os.path.join(os.path.dirname("__file__"),'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_directory))

hidden_html="""
<input type="hidden" name="food" value="%s">
"""

item_html="""
<li>%s</li>
"""
shopping_list_html="""
<br><br>
<h2>Shopping List</h2>
<ul>
%s
</ul>
"""
class MainHandler(webapp2.RequestHandler):
    def render_string(self, template,09params):
        t = jinja_end.get_template(template)
        return t.render(params)
    def render(self, template, **params):
        self.response.out.write(self.render_string(template, params))
    def write(self, *args, *kwargs):
        self.response.out.write(*args, *kwargs)

    def get(self):
        output=form_html
        output_hidden=""
        output_items=""
        items=self.request.get_all('food')
        if items:
            for item in items:
                output_hidden += hidden_html%item
                output_items += item_html%item

            output_shopping=shopping_list_html%output_items
            output+=output_shopping

        output = output%output_hidden
        self.response.write(output)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
