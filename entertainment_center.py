# -*- coding: utf-8 -*-

#importing media.py file into this file 
import media
#importing fresh_tomatoes.py file into this file
import fresh_tomatoes

Idiots = media.Movie("3 Idiots",
        "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
	"https://youtu.be/xvszmNXdM4w")

Blackpanther = media.Movie("Black Panther",
	"https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
	"https://youtu.be/xjDjIWPwcPU")

Zero=media.Movie("Zero",
	"https://upload.wikimedia.org/wikipedia/en/7/77/Zero_first_look_poster.jpg",
	"https://youtu.be/RF7DhGIQE1k")

Insideout=media.Movie("Inside Out",
	"https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
	"https://youtu.be/seMwpP0yeu4")

Hatestory=media.Movie("Hate Story 4",
	"https://upload.wikimedia.org/wikipedia/en/9/9a/Hate_Story_4_Official_Poster.jpg",
	"https://youtu.be/0B7athiVJBA")

Midnightsun=media.Movie("Midnight Sun",
	"https://upload.wikimedia.org/wikipedia/en/6/65/Midnight_Sun_2017.jpg",
	"https://youtu.be/fEskVQgtwaI")

#list of movies
movies = [Idiots, Blackpanther, Zero, Insideout, Hatestory, Midnightsun]

#calling of fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)

