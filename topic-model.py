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


processed_docs = [preprocess_text(purpose) for purpose in purposes]

dictionary = gensim.corpora.Dictionary(processed_docs)
dictionary.filter_extremes()
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

tfidf = gensim.models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

from pprint import pprint
for doc in corpus_tfidf:
    pprint(doc)
    break