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


[preprocess_text(purpose) for purpose in purposes]