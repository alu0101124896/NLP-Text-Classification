#! /bin/python

#
# File: vocabulary-parser.py
# Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
# Since: Sprint 2021
# College: University of La Laguna
# Degree: Computer Science - Advanced Artificial Intelligence
# Description: This program obtains the vocabulary of the given descriptions,
#  in this case, the second column of the given csv file.
#

import nltk
nltk.download('stopwords')

import re


def main():
  """
  Main function to obtain the vocabulary form the given csv file
  """
  inputFile = input("\nInput file: ")
  outputFile = input("\nOutput file: ")

  rawData = open(inputFile, "r").read().split("\n")

  if rawData[-1] == "":
    rawData.pop()

  descriptions = extractDescriptions(rawData)
  vocabulary = extractVocabulary(descriptions)

  exportToFile(outputFile, vocabulary)


def extractDescriptions(rawData):
  """
  Function to extract the descriptions from de rest of the data base
  """
  descriptions = []

  for line in rawData:
    descriptions.append(line.split(",")[1])
    # This time, the column separator in the csv file is a comma (,)

  return descriptions


def extractVocabulary(descriptions):
  """
  Function to extract the vocabulary from the
  """
  tokens = set()
  for sentence in descriptions:
    sentence = sentence.lower()
    sentence = removeNonAlphanumChars(sentence)
    sentence = removeExtraWhitespaces(sentence)
    tokens.update(wordTokenize(sentence))

  tokens = removeStopwords(tokens)

  vocabulary = list(tokens)
  vocabulary.sort()

  if vocabulary[0] == "":
    vocabulary.pop(0)

  return vocabulary


def removeNonAlphanumChars(sentence):
  """
  Function to replace the non alphanumeric characters with whitespaces
  """
  return re.sub(r"[^a-z0-9]", " ", sentence)


def removeExtraWhitespaces(sentence):
  """
  Function to remove whitespaces when there are two or more next to each other
  """
  return " ".join(sentence.strip().split())


def wordTokenize(sentence):
  """
  Function to obtain a set composed by the words of the given sentence
  """
  return set(sentence.split(" "))


def removeStopwords(tokens):
  """
  Function to remove the stopwords from the vocabulary
  """
  stopwords = " ".join(nltk.corpus.stopwords.words("english"))
  stopwords = stopwords.lower()
  stopwords = removeNonAlphanumChars(stopwords)
  stopwords = removeExtraWhitespaces(stopwords)
  stopwordsSet = wordTokenize(stopwords)

  tokens.difference_update(stopwordsSet)

  return tokens


def exportToFile(outputFile, vocabulary):
  """
  Function to export the vocabulary to a file
  """
  with open(outputFile, "w") as f:
    print("Numero de palabras:", len(vocabulary), file=f)

    for word in vocabulary:
      print(word, file=f)


main()
