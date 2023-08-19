import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")
all_movies = soup.find_all(name="h3", class_= "listicleItem_listicle-item__title__hW_Kn")
movie_titles = [ movie.getText() for movie in all_movies][::-1]

with open("movies.text", "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")