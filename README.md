# ETL process 

#### Main features

  - Data scraper
  - Python script which transforms data from
  text to different types and load them to csv file.
  - Machine learning algorithm that clasifie reviews as positive/neutral/negative
  - Script that loads CSV file to postgressSQL database 
  - Flask with dockerized PostgreSQL database 

##### Extract

  - It scrapas data from IMDB using BeautifulSoup
  - Scraper takes some number of most popular movies and exteact details
  - Then loads it to a csv file in raw text form

### Tech
* [Python] - Main backend programming language
* [BeautifulSoup] - Web scraper
* [TensorFlow] - Used in ML algorithm
* [Docker] - just docker
* [Flask] - web framework
* [PostgreSQL] - database
* [Bootstrap] - web web web
* [Datatables] - fun with tables

### Setup postgres

```
docker run --name etl_imdb -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=imdb -d -p 5432:5432 postgres
```
###Install requirements
pip install ./etl_process/requirements.txt

### How to run
In terminal:
```
python wsgi.py
```
