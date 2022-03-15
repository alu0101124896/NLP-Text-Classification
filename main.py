#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: main.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Sprint 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program estimates the probabilities of the languaje model
 from given train corpus and classifies the given test corpus documents into
 the learned classes
"""

import time

from src.vocabulary_parser import parse_vocabulary
from src.classes_parser import parse_classes
from src.corpus_parser import split_corpus, corpus_to_test
from src.probabilities_estimator import estimate_probabilities
from src.corpus_classifier import classify_corpus, check_precision


def main():
    """
    Function to execute everything at once
    """
    start = time.perf_counter()

    # corpusFile = input("Main corpus input file (Default = ./data/ecom-train.csv):"
    #                    ) or "./data/ecom-train.csv"
    corpus_file = "./data/ecom-train.csv"

    parse_vocabulary(input_file=corpus_file, output_to_file=True)
    parse_classes(input_file=corpus_file, output_to_file=True)
    split_corpus(input_file=corpus_file, output_to_file=True)
    estimate_probabilities(output_to_file=True)
    corpus_to_test(input_file=corpus_file, output_to_file=True)
    classify_corpus(output_to_file=True)
    check_precision(original_file=corpus_file)

    end = time.perf_counter()
    print(f"\nThe time spent in the main function was {end - start} seconds")


if __name__ == "__main__":
    main()
