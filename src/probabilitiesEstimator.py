#
# File: probabilitiesEstimator.py
# Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
# Since: Sprint 2021
# College: University of La Laguna
# Degree: Computer Science - Advanced Artificial Intelligence
# Description: This program estimates the probability values of every word in
#  the vocabulary for each class corpus
#

import math
import time

from dataGetters import classesData, classCorpusData, vocabularyData


def estimateProbabilities():
  """
  Main function to estimate the probability values of every word in the
   vocabulary for each class corpus
  """
  _, classes = classesData()
  vocabularySize, vocabulary = vocabularyData()

  Kunk = 0  # unknown word umbral value
  start = time.perf_counter()

  for className in classes:
    print(f"Estimating {className} class probabilities...")
    documentsInClassCorpus, wordsInClassCorpus, classCorpusWords = \
      classCorpusData(className)

    if vocabulary[-1] == "<unk>":
      frequenciesList = [
          classCorpusWords.count(word) for word in vocabulary[:-1]
      ]
    else:
      frequenciesList = [classCorpusWords.count(word) for word in vocabulary]

    frequeciesList = [
        freq if freq > Kunk else 0 for freq in frequenciesList
    ]

    if vocabulary[-1] == "<unk>":
      frequeciesList.append(Kunk)  # unknown word frequency = Kunk

    classProbabilities = list(
        map(
            lambda word, frequency: {
                "word":
                word,
                "freq":
                frequency,
                "logProb":
                math.log((frequency + 1) /
                         (wordsInClassCorpus + vocabularySize))
            }, vocabulary, frequeciesList))

    exportToFile(className, documentsInClassCorpus, wordsInClassCorpus,
                 classProbabilities)

  end = time.perf_counter()
  print(f"Time spent estimating probabilities: {end - start} seconds")


def exportToFile(className, documentsInClassCorpus, wordsInClassCorpus,
                 classProbabilities):
  """
  Function to export the class probabilities to a file
  """
  outputFile = "../data/aprendizaje" + className[0] + ".txt"

  with open(outputFile, "w", encoding='utf-8-sig') as f:
    print(f"Numero de documentos del corpus: {documentsInClassCorpus}", file=f)
    print(f"Numero de palabras del corpus: {wordsInClassCorpus}", file=f)

    for wordData in classProbabilities:
      print(f"Palabra: {wordData.get('word')}",
            f"Frec: {wordData.get('freq')}",
            f"LogProb: {wordData.get('logProb')}",
            file=f)


# estimateProbabilities()
