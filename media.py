6666666666666666666666666666666# -*- coding: utf-8 -*-

#importing web module into it
import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self,title,poster,trailer):
        # initialize instance of class Movie
        self.title=title
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer

    def show_trailer(trailer):
    	#Shows trailer of Movie
    	webbrowser.open(trailer)

