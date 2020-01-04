#!/usr/bin/env python
# coding: utf-8

# In[10]:


import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd


# In[11]:


MODEL_NAME = 'model.h5'
CSV_FILE_NAME = '../csv_files/movies_reviews.csv'
GENERETED_FILE_WITH_RATING_NAME = 'movies_reviews_and_predictions.csv'


# In[12]:


def load_data_model_and_csv():
    '''Loading all data sources'''
    data = keras.datasets.imdb
    model = keras.models.load_model(MODEL_NAME)
    movies_reviews = pd.read_csv(CSV_FILE_NAME)
    return data, model, movies_reviews


# In[13]:


def make_word_index():
    '''Loading and modyfing word index dictionary'''
    word_index = data.get_word_index()
    word_index = {k:(v+3) for k,v in word_index.items()}
    word_index["<PAD>"] = 0
    word_index["<START>"] = 1
    word_index["<UNK>"] = 2
    word_index["<INUSED>"] = 3
    return word_index


# In[14]:


def  review_encode(text):
    '''Encoding words from text to dictionary'''
    encoded = [1]
    for word in text:
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(2)
    return encoded


# In[15]:


def format_review(review_string):
    '''Formating reviews string and separating them to list elements.'''
    
    review_string.replace(',', '').replace(',', '').replace('.', '').replace('(', '').replace(')', '').replace('\"', '').replace(':', '').replace('\n', ' ').replace('\r', '')
    
    return review_string


# In[16]:


def apply_model_and_add_rating_to_df():
    movies_reviews.loc[:,'Reviews'] = movies_reviews.loc[:,'Reviews'].apply(format_review)
    movies_reviews.loc[:,'Encoded_Reviews'] = movies_reviews.loc[:,'Reviews'].apply(review_encode)
    movies_reviews.loc[:,'Preprocessed_Reviews'] = [keras.preprocessing.sequence.pad_sequences(k, value = word_index["<PAD>"], padding="post", maxlen = 250) for index, k in movies_reviews[['Encoded_Reviews']].iterrows()]
    movies_reviews.loc[:,'Preprocessed_Reviews'] = [keras.preprocessing.sequence.pad_sequences(k, value = word_index["<PAD>"],) for index, k in movies_reviews[['Encoded_Reviews']].iterrows()]
    movies_reviews.loc[:,'Preprocessed_Reviews'] = movies_reviews.loc[:,'Preprocessed_Reviews'].apply(model.predict)
    movies_reviews.loc[:,'Preprocessed_Reviews'] = movies_reviews.loc[:,'Preprocessed_Reviews'].apply(np.squeeze)
    movies_reviews.drop('Encoded_Reviews', axis=1, inplace=True)
    movies_reviews.rename({'Preprocessed_Reviews': 'Rating'}, axis=1, inplace=True)


# In[17]:


def generate_csv_with_rating():
    '''Generate csv file witch predictions based on reviews by applying ml model.'''
    movies_reviews.to_csv(GENERETED_FILE_WITH_RATING_NAME)


# In[18]:





# In[19]:


# generate_csv_with_rating()
def run_rating_generate(rootpath):
    CSV_PATH = rootpath+'/csv_files/'
    global CSV_FILE_NAME
    global GENERETED_FILE_WITH_RATING_NAME
    global MODEL_NAME
    CSV_FILE_NAME = CSV_PATH + 'movies_reviews.csv'
    GENERETED_FILE_WITH_RATING_NAME = CSV_PATH + 'movies_reviews_and_predictions.csv'
    MODEL_NAME = rootpath + '/transform_part/model.h5'
    global data
    global model
    global movies_reviews
    global word_index
    data, model, movies_reviews = load_data_model_and_csv()
    word_index = make_word_index()
    apply_model_and_add_rating_to_df()
    generate_csv_with_rating()


# In[ ]:



