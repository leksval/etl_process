
import pandas as pd
import numpy as np
from datetime import date
import re

INPUT_CSV_FILE_NAME = 'extracted_movies.csv'
MOVIES_DETAILS_CSV_NAME = 'movies_details.csv'
MOVIES_CAST_CSV_NAME = 'movies_cast.csv'
MOVIES_REVIEWS_CSV_NAME = 'movies_reviews.csv'
CSV_PATH = '../csv_files/'
END_REVIEW_TOKEN = '$&&&&$'

def create_row_for_each_list_element(df, list_column_to_split):
    '''Creating row in dataframe for each list element.'''

    extended_df = pd.DataFrame({
                        col:np.repeat(df[col].values, df[list_column_to_split].str.len())
                        for col in df.columns.drop(list_column_to_split)
                        }).assign(**{list_column_to_split:np.concatenate(df[list_column_to_split].values)})[df.columns]
    return extended_df



def movies_details_to_csv(movies):
    movies_details = movies[['Title', 'Year', 'Director', 'Movie summary']].copy()

    movies_details.loc[:,'Title'] = movies_details.loc[:,'Title'].str.strip()
    # oczyszczanie kolumny 'Title' z niepotrzebnych białych znaków

    movies_details.loc[:,'Year'] = movies_details.loc[:,'Year'].str.extract(r'(\d+)') #.astype(int)
    # wyciągnięcie numeru z kolumny 'Year' i zmiana na int

    movies_details.loc[:,'Director'] = movies_details.loc[:,'Director'].str.replace("\nDirector:\n", "").str.replace("\nDirectors:\n", "")
    # wyciągnięcie z kolumny 'Title' imię i nazwisko reżysera

    movies_details.insert(loc = 0, column='Ranking Position', value = movies_details.index + 1)
    movies_details.insert(loc = 0, column='Ranking Date', value = date.today())

    movies_details

    movies_details.to_csv(CSV_PATH + MOVIES_DETAILS_CSV_NAME, index=False)

#####################################################################################
def movies_reviews_to_csv(movies):

    movies_reviews = movies.filter(['Title', 'Reviews'], axis=1)

    def format_reviews(reviews_string):
        '''Formating reviews string and separating them to list elements.'''
        END_REVIEW_TOKEN = '$&&&&$'
        reviews_list = list(reviews_string.replace("[", "")
                                        .replace("]", "")
                                        .replace("\'", "")
                                        .replace("\\", "")
                                        .replace("\\t", "")
                                        .replace("\\s", "")
                                        .replace("\\m", "")
                                        .replace(', "', " ")
                                        .strip()
                                        .replace(END_REVIEW_TOKEN + '"', END_REVIEW_TOKEN)
                                        .split(END_REVIEW_TOKEN))
        
        del reviews_list[-1]
        return reviews_list

    movies_reviews.loc[:,'Reviews'] = movies_reviews.loc[:,'Reviews'].apply(format_reviews)



    movies_reviews = create_row_for_each_list_element(movies_reviews, 'Reviews')

    movies_reviews.to_csv(CSV_PATH + MOVIES_REVIEWS_CSV_NAME, index=False)

###########################################################################################

def movies_cast_to_csv(movies):

    movies_cast = movies.filter(['Title', 'Cast'], axis=1)

    def from_string_to_list_on_cast(cast_string):
        '''Modifing cast string and saving results to list'''
        #przetworzenie stringu na listę aktorzy i role w jednej tabeli
        #aktorzy nieparzyści, role parzyste
        cast_string = list(cast_string.replace("\n", "")
                                  .strip()
                                  .replace("\\n", "")
                                  .replace("'", "").replace("[  ", "")
                                  .replace("]", "")
                                  .replace("               ...          ", ": ")
                                  .replace(':', ",   ") # delete role names
                                  .split(",   "))
        #przekonwertowanie lna liste aktor:rola
        cast_list = cast_string[::2]
        return cast_list

    movies_cast.loc[:,'Cast'] = movies_cast.loc[:,'Cast'].apply(from_string_to_list_on_cast)

    movies_cast = create_row_for_each_list_element(movies_cast, 'Cast')

    movies_cast.to_csv(CSV_PATH +MOVIES_CAST_CSV_NAME, index=False)

def transform_and_generate_files():

    movies = pd.read_csv(CSV_PATH + INPUT_CSV_FILE_NAME)

    movies_details_to_csv(movies)
    movies_reviews_to_csv(movies)
    movies_cast_to_csv(movies)

transform_and_generate_files()