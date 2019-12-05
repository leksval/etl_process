# %%
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd

# %%
data = keras.datasets.imdb

# %%
(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000)
# only words that appera over 10000 times

# %%


# %%
word_index = data.get_word_index()

# %%
word_index = {k:(v+3) for k,v in word_index.items()}

# %%
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<INUSED>"] = 3

# %%
reverse_word_index = dict([(value, key) for (key,value) in word_index.items()])

# %%
train_data = keras.preprocessing.sequence.pad_sequences(train_data, value = word_index["<PAD>"], padding="post", maxlen = 250)
test_data  = keras.preprocessing.sequence.pad_sequences(test_data, value = word_index["<PAD>"], padding="post", maxlen = 250)
# data must have the same len

# %%
print(len(test_data[0]),len(test_data[3]))

# %%
def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])

# %%
print(decode_review(test_data[0]))

# %%
# now defining model
model = keras.Sequential()
model.add(keras.layers.Embedding(88000, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1,  activation="sigmoid"))

# %%
model.summary()

# %%
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
x_val = train_data[:10000]
x_train = train_data[10000:]

y_val = train_labels[:10000]
y_train = train_labels[10000:]

# %%
fitModel = model.fit(x_train, y_train, epochs = 35, batch_size = 512, validation_data = (x_val, y_val), verbose = 1)

# %%
result = model.evaluate(test_data, test_labels)
print(result)

# %%
test_review = test_data[0]
predict = model.predict([test_review])
print("Review: ")
print(decode_review(test_review))
print("Prediction: " + str(predict[0]))
print("Accual: " + str(test_labels[0]))
print(result)

# %%
def  review_encode(s):
    encoded = [1]
    for word in s:
        if word.lower() in word_index:
            encoded.append(word_index[word.lower()])
        else:
            encoded.append(2)
    return encoded

# %%
model.save("model.h5")

# %%
model = keras.models.load_model("model.h5")

# %%
with open("test.txt") as infile, open('output.txt', 'w') as outfile:
    outfile.write(infile.read().replace(',', '').replace(',', '').replace('.', '')
                  .replace('(', '').replace(')', '').replace('\"', '').replace(':', '')
                  .replace('\n', ' ').replace('\r', ''))
    

# %%


# %%
movies_reviews = pd.read_csv('movies_reviews.csv')

# %%
movies_reviews

# %%
def format_review(review_string):
    '''Formating reviews string and separating them to list elements.'''
    review_string.replace(',', '').replace(',', '').replace('.', '').replace('(', '').replace(')', '').replace('\"', '').replace(':', '').replace('\n', ' ').replace('\r', '')
    
    return review_string

# %%
movies_reviews.loc[:,'Reviews'] = movies_reviews.loc[:,'Reviews'].apply(format_review)

# %%
movies_reviews.loc[:,'Encoded_Reviews'] = movies_reviews.loc[:,'Reviews'].apply(review_encode)
movies_reviews

# %%

movies_reviews.loc[:,'Preprocessed_Reviews'] = [keras.preprocessing.sequence.pad_sequences( k,  value = word_index["<PAD>"], padding="post", maxlen = 250) for index, k in movies_reviews[['Encoded_Reviews']].iterrows()]

# %%


# %%
movies_reviews.loc[:,'Preprocessed_Reviews'] = [keras.preprocessing.sequence.pad_sequences( k,  value = word_index["<PAD>"],) for index, k in movies_reviews[['Encoded_Reviews']].iterrows()]

# %%
def prediction(m):
    b = model.predict(m)
    return b

# %%
movies_reviews.loc[:,'Preprocessed_Reviews'] = movies_reviews.loc[:,'Preprocessed_Reviews'].apply(model.predict)

# %%
movies_reviews.loc[:,'Preprocessed_Reviews']

# %%
movies_reviews.to_csv('movies_reviews_and_predictions')

# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%


# %%
