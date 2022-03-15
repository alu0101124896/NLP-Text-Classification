#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: preprocessing.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Sprint 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program implements some functions to preprocess the raw data
 from the given corpus
"""

import re

import nltk

nltk.download('stopwords')


def preprocess_data(corpus):
    """
    Function to preprocess the given corpus
    """
    stopwords = stopwords_data()

    corpus = list(map(lambda document: document.lower(), corpus))
    corpus = list(map(remove_non_alpha_chars, corpus))
    corpus = list(map(remove_extra_whitespaces, corpus))
    corpus = list(
        map(lambda document: remove_stopwords(document, stopwords), corpus))

    return corpus


def remove_non_alpha_chars(sentence):
    """
    Function to replace the non alphabetical characters with whitespaces
    """
    # return re.sub(r"\W", " ", sentence)
    # return re.sub(r"[^a-z0-9]", " ", sentence)
    return re.sub(r"[^a-z]", " ", sentence)


def remove_extra_whitespaces(sentence):
    """
    Function to remove whitespaces when there are two or more next to each other
    """
    return " ".join(sentence.strip().split())


def stopwords_data():
    """
    Function to obtain a list of preprocessed stopwords
    """
    stopwords = " ".join(nltk.corpus.stopwords.words("english"))
    stopwords = stopwords.lower()
    stopwords = remove_non_alpha_chars(stopwords)
    stopwords = remove_extra_whitespaces(stopwords)
    stopwords = list(set(stopwords.split()))

    return stopwords


def remove_stopwords(document, stopwords):
    """
    Function to remove the stopwords from the given string
    """
    return list(filter(lambda word: word not in stopwords, document.split()))
