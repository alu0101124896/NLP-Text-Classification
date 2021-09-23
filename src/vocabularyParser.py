#
# File: vocabularyParser.py
# Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
# Since: Sprint 2021
# College: University of La Laguna
# Degree: Computer Science - Advanced Artificial Intelligence
# Description: This program obtains the vocabulary of the given descriptions,
#  in this case, the second column of the given csv file.
#

from itertools import chain

from dataGetters import getRawData
from corpusParser import extractDescriptions
from preprocessing import preprocessData


def parseVocabulary(inputFile="../data/ecom-train.csv",
                    outputFile="../data/vocabulario.txt"):
  """
  Main function to obtain the vocabulary form the given csv file
  """
  print("Parsing vocabulary...")

  rawData = getRawData(inputFile)
  descriptions = extractDescriptions(rawData)
  vocabulary = extractVocabulary(descriptions)

  vocabulary.append("<unk>")

  exportToFile(vocabulary, outputFile)


def extractVocabulary(descriptions):
  """
  Function to extract the vocabulary from the given descriptions
  """

  descriptions = preprocessData(descriptions)
  tokens = set(chain(*descriptions))

  vocabulary = list(tokens)
  vocabulary.sort()

  return vocabulary


def exportToFile(vocabulary, outputFile):
  """
  Function to export the vocabulary to a file
  """
  with open(outputFile, "w", encoding='utf-8-sig') as f:
    print(f"Numero de palabras: {len(vocabulary)}", file=f)

    for word in vocabulary:
      print(word, file=f)


# parseVocabulary()
