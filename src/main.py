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
from corpusParser import splitCorpus
from probabilitiesEstimator import estimateProbabilities


def main():
  """
  Function to execute everything at once
  """
  start = time.perf_counter()

  parseVocabulary()
  parseClasses()
  splitCorpus()
  estimateProbabilities()

  end = time.perf_counter()
  print(f"Time spent in main function is: {end - start} seconds")


main()
