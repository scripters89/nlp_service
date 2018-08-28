#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 19:51:58 2018

@author: mashiksa
"""
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction import stop_words
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
from gensim.models import Word2Vec
import spacy
from nltk.tokenize import RegexpTokenizer
from flask import make_response

def pre_process(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text.lower())
    lemmatizer = WordNetLemmatizer().lemmatize
    stops = stopwords.words('english')
    tokens = list(map(lambda x: lemmatizer(lemmatizer(x,'n'),'v'), filter(lambda x: x not in stops, tokens)))
    return tokens


def wordEmbed(text):
    nlp = spacy.load('en')
    return nlp(' '.join(pre_process(text))).vector
    
def health_check():
    return make_response('{"ok": "OK!"}', 200)


def ping():
    return make_response('{"ok": "Pong!"}', 200)

if __name__ == "__main__":
    import nltk