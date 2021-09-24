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


def realDocumentClassesData(inputFile="../data/ecom-train.csv"):
  """
  Function to obtain the real document classes data from the given file
  """
  classes = getRawData(inputFile)

  return list(map(lambda document: document.split(",")[0][0], classes))


def classifiedDocumentClassesData(inputFile="../data/resumen-alu0101124896.csv"):
  """
  Function to obtain the classified document classes data from the given file
  """
  classes = getRawData(inputFile)

  if len(classes[0]) > 1:
    classes.pop(0)

  return classes


def classProbabilitiesData(className, inputFile=None):
  """
  Function to obtain the class probabilities data from the given file
  """
  if inputFile is None:
    inputFile = "../data/aprendizaje" + className[0] + ".txt"

  classProbabilities = getRawData(inputFile)

  documentsInClassCorpus = int(classProbabilities.pop(0).split()[-1])
  wordsInClassCorpus = int(classProbabilities.pop(0).split()[-1])

  classProbabilities = list(map(lambda line: line.split(), classProbabilities))
  classProbabilities = list(
      map(
          lambda line: {
              "word": line[1],
              "freq": int(line[3]),
              "logProb": float(line[5])
          }, classProbabilities))

  return documentsInClassCorpus, wordsInClassCorpus, classProbabilities


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


def testCorpusData(inputFile="../data/corpus-test.csv"):
  """
  Function to obtain the test corpus data from the given file
  """
  corpusRawData = getRawData(inputFile)
  corpus = preprocessData(corpusRawData)

  return len(corpus), corpus
