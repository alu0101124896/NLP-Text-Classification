#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: vocabulary_parser.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Sprint 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program obtains the vocabulary of the given descriptions,
  in this case, the second column of the given csv file.
"""

from itertools import chain

from src.data_getters import get_raw_data
from src.corpus_parser import extract_descriptions
from src.preprocessing import preprocess_data


def parse_vocabulary(input_file, output_to_file=False):
    """
    Main function to obtain the vocabulary form the given csv file
    """
    print("Parsing vocabulary...")

    corpus_raw_data = get_raw_data(input_file)
    descriptions = extract_descriptions(corpus_raw_data)
    vocabulary = extract_vocabulary(descriptions)

    vocabulary.append("<unk>")

    if output_to_file:
        # output_file = input(
        #     "Vocabulary output file (Default = ./data/vocabulario.txt):"
        # ) or "./data/vocabulario.txt"
        output_file = "./data/vocabulario.txt"

        export_to_file(vocabulary, output_file)

    return vocabulary


def extract_vocabulary(descriptions):
    """
    Function to extract the vocabulary from the given descriptions
    """
    descriptions = preprocess_data(descriptions)
    tokens = set(chain(*descriptions))

    vocabulary = list(tokens)
    vocabulary.sort()

    return vocabulary


def export_to_file(vocabulary, output_file):
    """
    Function to export the vocabulary to a file
    """
    with open(output_file, "w", encoding='utf-8-sig') as file:
        print(f"Numero de palabras: {len(vocabulary)}", file=file)

        for word in vocabulary:
            print(word, file=file)


if __name__ == "__main__":
    parse_vocabulary("./data/ecom-train.csv")
