#
# File: corpusClassifier.py
# Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
# Since: Sprint 2021
# College: University of La Laguna
# Degree: Computer Science - Advanced Artificial Intelligence
# Description: This program classifies the test corpus into the learned classes
#

import time

from dataGetters import getRawData, vocabularyData, classesData
from dataGetters import realDocumentClassesData, classifiedDocumentClassesData
from dataGetters import classProbabilitiesData, testCorpusData


def classifyCorpus(inputFile="../data/corpus-test.csv"):
  """
  Function to classify the test corpus documents into the learned classes
  """
  studentCode = input("Código de alumno: ")

  print("Classifying documents...")

  testCorpusSize, testCorpus = testCorpusData(inputFile)
  numOfClasses, classes = classesData()
  vocabularySize, vocabulary = vocabularyData()

  unkIndex = -1  # last item on the vocabulary list

  start = time.perf_counter()

  resultsList = list(map(lambda document: [document], getRawData(inputFile)))

  classProbabilitiesList = list(
      map(lambda className: classProbabilitiesData(className), classes))

  for classProbabilities in classProbabilitiesList:
    if vocabularySize != len(classProbabilities[2]):
      raise ValueError(
          "The vocabulary doesn't correstpond to the class probabilities")

  for documentIndex in range(len(testCorpus)):
    for documentsInClassCorpus, _, classProbabilities in classProbabilitiesList:
      indexList = list()

      for word in testCorpus[documentIndex]:
        try:
          indexList.append(vocabulary.index(word))

        except ValueError:
          indexList.append(unkIndex)

      currentDocumentWordsLogProbs = [
          classProbabilities[wordIndex]["logProb"] for wordIndex in indexList
      ]

      classLogProb = documentsInClassCorpus / testCorpusSize
      currentDocumentLogProb = sum(currentDocumentWordsLogProbs, classLogProb)

      resultsList[documentIndex].append(currentDocumentLogProb)

    bestDocumentLogProb = max(resultsList[documentIndex][1:numOfClasses + 1])
    bestClassIndex = resultsList[documentIndex].index(bestDocumentLogProb) - 1

    resultsList[documentIndex].append(classes[bestClassIndex][0])

  end = time.perf_counter()
  print(f"Time spent classifying is: {end - start}")

  print("Exporting to files...")
  exportToFile(resultsList, numOfClasses, studentCode)


def checkPrecision(originalFile="../data/ecom-train.csv",
                   classifiedFile="../data/resumen-train.csv"):
  """
  Function to check the precision on the classified descriptions
  """
  print("Checking precision...")

  realClasses = realDocumentClassesData(originalFile)
  resultsList = classifiedDocumentClassesData(classifiedFile)

  guessedClasses = list(
      map(lambda result, real: result[-1] == real, resultsList, realClasses))

  numOfGuessedDocuments = len(guessedClasses) - guessedClasses.count(False)
  successRate = numOfGuessedDocuments * 100 / len(guessedClasses)

  print(numOfGuessedDocuments, "of", len(guessedClasses))
  print("Success rate:", str(successRate) + "%")


def exportToFile(resultsList, numOfClasses, studentCode):
  """
  Function to export the classified descriptions to a file
  """
  classifyOutputFile = "../data/clasificacion-alu0101124896.csv"
  resumeOutputFile = "../data/resumen-alu0101124896.csv"

  with open(classifyOutputFile, "w", encoding='utf-8-sig') as cf:
    with open(resumeOutputFile, "w", encoding='utf-8-sig') as rf:
      print(f"Código: {studentCode}", file=rf)

      for result in resultsList:
        print(result[0], end=",", file=cf)

        for index in range(numOfClasses):
          print(round(result[index + 1], 2), end=",", file=cf)

        print(result[-1], file=cf)
        print(result[-1], file=rf)


# classifyCorpus()
# checkPrecision()

# classifyCorpus(inputFile="../data/ecom-test.csv")
# checkPrecision(originalFile="../data/ecom-test-check-20.csv",
#                classifiedFile="../data/resumen-alu0101124896.csv")
