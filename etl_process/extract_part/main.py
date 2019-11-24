from bs4 import BeautifulSoup
from datetime import date
import requests
# import random


def get_most_popular_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn", limit=10)
    # random.shuffle(movies)
    return movies


def get_movie_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    return soup.find("div", class_="summary_text").contents[0].strip()


def get_movie_title_and_year(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    original_title = soup.find("div", class_="originalTitle")
    title = soup.find("h1").text.split('(')[0]
    year = soup.find("span", id="titleYear").text
    return title if original_title is None else original_title.text.split('(')[0], year


def get_movies_urls(movie):
    # movie_title = movie.a.contents[0]
    # movie_year = movie.span.contents[0]
    movie_url = 'http://www.imdb.com' + movie.a['href']
    movie_reviews_url = movie_url + 'reviews'
    return movie_url, movie_reviews_url


def get_movie_reviews(movie_reviews_url):
    page = requests.get(movie_reviews_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    reviews = [review.text for review in soup.find_all('div', class_="text", limit=10)]
    return reviews


def most_popular_movies_on_imdb():
    today = date.today()
    print("Today's date:", today)
    print("--------------------------------------------")
    for movie in get_most_popular_movies('https://www.imdb.com/chart/moviemeter'):
        movie_url, movie_reviews_url = get_movies_urls(movie)
        movie_summary = get_movie_summary(movie_url)
        # print(movie_title, movie_year)

        # moja funkcja pozyskiwnia tytułu i roku
        title, year = get_movie_title_and_year(movie_url)
        print(title, year)
        print(movie_summary)

        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")

        for rev in get_movie_reviews(movie_reviews_url):
            print(rev)
            print("++++++++++++++++++++++++++++++++++++++++++++")

        print("--------------------------------------------")


if __name__ == '__main__':
    most_popular_movies_on_imdb()
