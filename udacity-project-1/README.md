# Favorite Movie Trailers (Fresh Tomatoes)

This app is a collection of my favorite movies. It allows you to view the poster, and trailer for the added favorite movies.

## Static App (Original Project)

This is the application as per the original requirements of the project.
To run, navigate to [`static-app`](static-app) directory
```shell
python fresh_tomatoes.py
```
####Note ensure you're in the [`static-app`](static-app) directory before running otherwise it will not find the shared classes in the ../dynamic-app/lib folder

## Dynamic App (Extension)

I took the liberty to use some of the knowledge I gained in the Intro to Backend course and built on top of the static page by adding a form to add new movies to the page.

Load the [`dynamic-app`](dynamic-app) directory in google app engine launcher. Hit run.
Type `http://localhost:8080/` in your browser of choice.

### [`main.py`](dynamic-app/main.py)

Implements the google app engine server request handler. Main entry point for the page for all incoming GET and POST requests. It uses the shared components to store movie related data


# Shared Classes
These are the classes shared between both the static and dynamic page. They are the primary classes that store the information rendered by both the static and dynamic pages.

### [`entertainment_center.py`](dynamic-app/lib/entertainment_center.py)

Holds a list of movie types.


### [`movie.py`](dynamic-app/lib/movie.py)

Defines the properties and template for a movie


## Shortcomings in current design

* One of the biggest short commings is that the page doesn't  store all the movie related information in a database. It currently stores all the information in a hidden form field, with a special delimited string. This is obviously very hacky and should be fixed once I learn about databases