#! /bin/python

#
# File: main.py
# Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
# Since: Sprint 2021
# College: University of La Laguna
# Degree: Computer Science - Advanced Artificial Intelligence
# Description: This program estimates the probabilities of the languaje model
#  from given train corpus and classifies the given test corpus documents into
#  the learned classes
#

import time

from vocabularyParser import parseVocabulary
from classesParser import parseClasses
from corpusParser import splitCorpus, corpusToTestFile
from probabilitiesEstimator import estimateProbabilities
from corpusClassifier import classifyCorpus, checkPrecision


def main():
  """
  Function to execute everything at once
  """
  start = time.perf_counter()

  corpusFile = input("Main corpus file (Default = ../data/ecom-train.csv):") \
    or "../data/ecom-train.csv"
  testCorpusFile = input("Test corpus file (Default = ../data/corpus-test.csv):") \
    or "../data/corpus-test.csv"

  parseVocabulary(inputFile=corpusFile)
  parseClasses(inputFile=corpusFile)
  splitCorpus(inputFile=corpusFile)
  estimateProbabilities()
  corpusToTestFile(inputFile=corpusFile)
  classifyCorpus(inputFile=testCorpusFile)
  checkPrecision(originalFile=corpusFile)

  end = time.perf_counter()
  print(f"Time spent in main function is: {end - start} seconds")


main()
