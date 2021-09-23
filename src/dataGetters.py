#
# File: dataGetters.py
# Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
# Since: Sprint 2021
# College: University of La Laguna
# Degree: Computer Science - Advanced Artificial Intelligence
# Description: This program implements some functions to get data from files
#

from itertools import chain

from preprocessing import preprocessData


def getRawData(inputFile):
  """
  Function to obtain the raw data from the given file
  """
  rawData = open(inputFile, "r", encoding='utf-8-sig').read().split("\n")

  if rawData[-1] == "":
    rawData.pop()

  return rawData


def vocabularyData(inputFile="../data/vocabulario.txt"):
  """
  Function to obtain the vocabulary data from the given file
  """
  vocabulary = getRawData(inputFile)

  vocabularySize = int(vocabulary.pop(0).split().pop())

  return vocabularySize, vocabulary


def classesData(inputFile="../data/clases.txt"):
  """
  Function to obtain the classes data from the given file
  """
  classes = getRawData(inputFile)

  numOfClasses = int(classes.pop(0).split().pop())

  return numOfClasses, classes


def classCorpusData(className, inputFile=None):
  """
  Function to obtain the class corpus data from the given file
  """
  if inputFile is None:
    inputFile = "../data/corpus" + className[0] + ".txt"

  corpusRawData = getRawData(inputFile)
  corpus = preprocessData(corpusRawData)
  corpusWords = list(chain(*corpus))

  return len(corpus), len(corpusWords), corpusWords
