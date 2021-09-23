#
# File: corpusParser.py
# Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
# Since: Sprint 2021
# College: University of La Laguna
# Degree: Computer Science - Advanced Artificial Intelligence
# Description: This program splits the given corpus into diferent corpus with
#  the same class type documents
#

from dataGetters import getRawData


def splitCorpus(inputFile="../data/ecom-train.csv"):
  """
  Function to split the given corpus into diferent corpus with the same class
   type documents
  """
  print("Splitting corpus...")

  corpusRawData = getRawData(inputFile)
  classes = extractClasses(corpusRawData)

  for className in classes:
    classDescriptions = extractDescriptions(corpusRawData, className)

    outputFile = "../data/corpus" + className[0] + ".txt"
    exportToFile(classDescriptions, outputFile)


def extractClasses(corpusRawData):
  """
  Function to extract the classes from de rest of the data base
  """
  return set(map(lambda line: line.split(",")[0], corpusRawData))


def extractDescriptions(corpusRawData, className=None):
  """
  Function to extract the descriptions from de rest of the data base
  """
  corpus = list(map(lambda line: line.split(","), corpusRawData))

  descriptions = [
      line[1] for line in corpus if className is None or line[0] == className
  ]

  return descriptions


def exportToFile(descriptions, outputFile):
  """
  Function to export the descriptions to a file
  """
  with open(outputFile, "w", encoding='utf-8-sig') as f:
    for description in descriptions:
      print(description, file=f)


# splitCorpus()
