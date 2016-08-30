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

form="""
What color is poop? Please answer in jeopardy format <br>
<form>
<select name="q">
<option value="1">One</option>
<option>Two</option>
<option>Three</option>
</select>
<br>
<input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self): # this will be invoked on GET request type
        self.response.write(form)


class FormHandler(webapp2.RequestHandler):
    def post(self): # this will be invoked on POST request
    	# post method HIDES parameters from url. parameters avaialble after HTTP headers
		# formValue = self.request.get('q')
		# self.response.write(formValue)
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(self.request)



app = webapp2.WSGIApplication([
    ('/', MainHandler), # you sub url + callback handler. i.e. URL Handler
    ('/testform', FormHandler)
], debug=True)
