#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: data_getters.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Sprint 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program implements some functions to get data from files
"""

from itertools import chain

from src.preprocessing import preprocess_data


def get_raw_data(input_file):
    """
    Function to obtain the raw data from the given file
    """
    with open(input_file, "r", encoding='utf-8-sig') as file:
        raw_data = file.read().split("\n")

        if raw_data[-1] == "":
            raw_data.pop()

        return raw_data


def vocabulary_data(input_file="./data/vocabulario.txt"):
    """
    Function to obtain the vocabulary data from the given file
    """
    vocabulary = get_raw_data(input_file)

    vocabulary_size = int(vocabulary.pop(0).split().pop())

    if vocabulary_size != len(vocabulary):
        raise AssertionError("Error: Unconsistent vocabulary size")

    return vocabulary_size, vocabulary


def classes_data(input_file="./data/clases.txt"):
    """
    Function to obtain the classes data from the given file
    """
    classes = get_raw_data(input_file)

    num_of_classes = int(classes.pop(0).split().pop())

    if num_of_classes != len(classes):
        raise AssertionError("Error: Unconsistent vocabulary size")

    return num_of_classes, classes


def raw_descriptions_data(input_file="./data/ecom-train.csv"):
    """
    Function to obtain the descriptions data from the given file
    """
    corpus_raw_data = get_raw_data(input_file)

    return [document.split(",")[-1] for document in corpus_raw_data]


def real_document_classes_data(input_file="./data/ecom-train.csv"):
    """
    Function to obtain the real document classes data from the given file
    """
    corpus_raw_data = get_raw_data(input_file)

    return [document.split(",")[0][0] for document in corpus_raw_data]


def classified_document_classes_data(
        input_file="./data/resumen-alu0101124896.csv"):
    """
    Function to obtain the classified document classes data from the given file
    """
    classes = get_raw_data(input_file)

    if len(classes[0]) > 1:  # If file has the 'código' line, delete it.
        classes.pop(0)

    return classes


def class_probabilities_data(class_name, input_file=None):
    """
    Function to obtain the class probabilities data from the given file
    """
    if input_file is None:
        input_file = f"./data/aprendizaje{class_name[0]}.txt"

    class_raw_cata = get_raw_data(input_file)

    documents_in_class_corpus = int(class_raw_cata.pop(0).split()[-1])
    words_in_class_corpus = int(class_raw_cata.pop(0).split()[-1])

    class_data = list(map(lambda line: line.split(), class_raw_cata))
    # classData = [ line.split() for line in classRawData ]

    class_probabilities = {
        line[1]: {
            "freq": int(line[3]),
            "logProb": float(line[5])
        }
        for line in class_data
    }

    class_data = {
        "documentsInClassCorpus": documents_in_class_corpus,
        "wordsInClassCorpus": words_in_class_corpus,
        "classProbabilities": class_probabilities
    }

    return class_data


def class_corpus_data(class_name, splitted_corpus, input_file=None):
    """
    Function to obtain the class corpus data from the given file
    """
    if splitted_corpus is None:
        if input_file is None:
            input_file = f"./data/corpus{class_name[0]}.txt"
        class_corpus_raw_data = get_raw_data(input_file)
    else:
        class_corpus_raw_data = splitted_corpus.get(class_name)

    corpus = preprocess_data(class_corpus_raw_data)
    corpus_words = list(chain(*corpus))

    return len(corpus), len(corpus_words), corpus_words


def test_corpus_data(input_file=None):
    """
    Function to obtain the test corpus data from the given file
    """
    if input_file is None:
        # inputFile = input(
        #     "Test corpus input file (Default = ./data/corpus-test.csv):"
        # ) or "./data/corpus-test.csv"
        input_file = "./data/corpus-test.csv"

    corpus_raw_data = get_raw_data(input_file)
    corpus = preprocess_data(corpus_raw_data)

    return len(corpus), corpus, input_file
