#
# File: classesParser.py
# Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
# Since: Sprint 2021
# College: University of La Laguna
# Degree: Computer Science - Advanced Artificial Intelligence
# Description: This program obtains the classes of the given descriptions,
#  in this case, the first column of the given csv file.
#

from corpusParser import extractClasses
from dataGetters import getRawData


def parseClasses(inputFile="../data/ecom-train.csv",
                 outputFile="../data/clases.txt"):
  """
  Main function to obtain the classes form the given csv file
  """
  print("Parsing classes...")

  # rawData = getRawData(inputFile)
  # classes = list(extractClasses(rawData))
  # classes.sort()

  # required in the next order for the classification output file format:
  classes = ["Household", "Books", "Clothing & Accessories", "Electronics"]

  exportToFile(classes, outputFile)


def exportToFile(classes, outputFile):
  """
  Function to export the classes to a file
  """
  with open(outputFile, "w", encoding='utf-8-sig') as f:
    print(f"Numero de clases: {len(classes)}", file=f)

    for className in classes:
      print(className, file=f)


# parseClasses()
