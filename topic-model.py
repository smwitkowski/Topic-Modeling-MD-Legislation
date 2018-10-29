import gensim
import numpy as np
import pandas as pd
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *


import nltk
nltk.download('wordnet')


def lemmatize_stemming(text):
    stemmer = SnowballStemmer("english")
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess_text(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if len(token) > 3 and token not in gensim.parsing.preprocessing.STOPWORDS:
            result.append(lemmatize_stemming(token))
    return result

data = pd.read_csv('C:\\Users\\switkowski\\Documents\\Projects\\Topic-Model-MD-Legislation\\legislation_scraper\\data\\bill_data.csv')
purposes = data[~data.purpose.isnull()].purpose.tolist()

processed_docs = [preprocess_text(purpose) for purpose in purposes]

dictionary = gensim.corpora.Dictionary(processed_docs)
dictionary.filter_extremes()
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

tfidf = gensim.models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lda_model = gensim.models.LdaMulticore(
    corpus_tfidf, num_topics=2, id2word=dictionary, passes=2, workers=3)