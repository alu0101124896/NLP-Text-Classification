#
# File: preprocessing.py
# Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
# Since: Sprint 2021
# College: University of La Laguna
# Degree: Computer Science - Advanced Artificial Intelligence
# Description: This program implements some functions to preprocess the raw data
#  from the given corpus
#

import nltk
nltk.download('stopwords')

import re


def preprocessData(corpus):
  """
  Function to preprocess the given corpus
  """
  stopwords = stopwordsData()

  corpus = list(map(lambda document: document.lower(), corpus))
  corpus = list(map(lambda document: removeNonAlphaChars(document), corpus))
  corpus = list(map(lambda document: removeExtraWhitespaces(document), corpus))
  corpus = list(
      map(lambda document: removeStopwords(document, stopwords), corpus))

  return corpus


def removeNonAlphaChars(sentence):
  """
  Function to replace the non alphabetical characters with whitespaces
  """
  # return re.sub(r"\W", " ", sentence)
  # return re.sub(r"[^a-z0-9]", " ", sentence)
  return re.sub(r"[^a-z]", " ", sentence)


def removeExtraWhitespaces(sentence):
  """
  Function to remove whitespaces when there are two or more next to each other
  """
  return " ".join(sentence.strip().split())


def stopwordsData():
  """
  Function to obtain a list of preprocessed stopwords
  """
  stopwords = " ".join(nltk.corpus.stopwords.words("english"))
  stopwords = stopwords.lower()
  stopwords = removeNonAlphaChars(stopwords)
  stopwords = removeExtraWhitespaces(stopwords)
  stopwords = list(set(stopwords.split()))

  return stopwords


def removeStopwords(document, stopwords):
  """
  Function to remove the stopwords from the given string
  """
  return list(filter(lambda word: word not in stopwords, document.split()))
