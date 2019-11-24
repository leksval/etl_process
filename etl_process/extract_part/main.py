from bs4 import BeautifulSoup
from datetime import date
import requests


def get_most_popular_movies(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    movies = soup.find_all("td", class_="titleColumn", limit=10)
    return movies


def get_movie_summary(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')
    return soup.find("div", class_="summary_text").contents[0].strip()


def get_movie_title_and_year(url):
    movie_page = requests.get(url)
    soup = BeautifulSoup(movie_page.text, 'html.parser')

    original_title = soup.find("div", class_="originalTitle")
    # w h1 podaje tytuł z dopiskiem original title w nawiasie więc przycinam
    title = soup.find("h1").text.split('(')[0]
    year = soup.find("span", id="titleYear").text
    director = soup.find("div", class_="credit_summary_item").text
    # Pierwsza wartość w cast to napis cast ovwrview
    cast = [review.text for review in soup.find_all('tr', limit=5)]
    return title if original_title is None else original_title.text.split('(')[0], year, director, cast


def get_movies_urls(movie):
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
        reviews = get_movie_reviews(movie_reviews_url)
        title, year, director, cast = get_movie_title_and_year(movie_url)
        reviews = [review for review in reviews]
        
        print(title, year)
        print(director)
        print(cast)
        print("_________________________________________")
        print(movie_summary)
        print("_________________________________________")
        print(*reviews, sep='\n ++++++++++++++++++++ \n')
        print("--------------------------------------------")


if __name__ == '__main__':
    most_popular_movies_on_imdb()
