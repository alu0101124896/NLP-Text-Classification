#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: corpus_parser.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Sprint 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program splits the given corpus into diferent corpus with
 the same class type documents
"""

from src.data_getters import classes_data, get_raw_data


def split_corpus(input_file, classes=None, output_to_file=False):
    """
    Function to split the given corpus into diferent corpus with the same class
    type documents
    """
    print("Splitting corpus...")

    corpus_raw_data = get_raw_data(input_file)

    if classes is None:
        _, classes = classes_data()

    splitted_corpus = {
        class_name: extract_descriptions(corpus_raw_data, class_name)
        for class_name in classes
    }

    if output_to_file:
        print("Exporting splitted corpuses to files...")
        for class_name, class_descriptions in splitted_corpus.items():
            # output_file = input(
            #     f"{class_name} class output file (Default = ./data/corpus{class_name[0]}.txt):"
            # ) or f"./data/corpus{class_name[0]}.txt"
            output_file = f"./data/corpus{class_name[0]}.txt"

            export_to_file(class_descriptions, output_file)

    return splitted_corpus


def corpus_to_test(input_file, output_to_file=False):
    """
    Function to delete the class column from the corpus file
    """
    print("Creating test file...")

    corpus_raw_data = get_raw_data(input_file)
    descriptions = extract_descriptions(corpus_raw_data)

    if output_to_file:
        # output_file = input(
        #     "Test corpus output file (Default = ./data/corpus-test.txt):"
        # ) or "./data/corpus-test.txt"
        output_file = "./data/corpus-test.csv"

        export_to_file(descriptions, output_file)

    return descriptions


def extract_classes(corpus_raw_data):
    """
    Function to extract the classes from de rest of the data base
    """
    return set(map(lambda line: line.split(",")[0], corpus_raw_data))


def extract_descriptions(corpus_raw_data, class_name=None):
    """
    Function to extract the descriptions from de rest of the data base
    """
    corpus = list(map(lambda line: line.split(","), corpus_raw_data))

    descriptions = [
        line[1] for line in corpus
        if class_name is None or line[0] == class_name
    ]

    return descriptions


def export_to_file(descriptions, output_file):
    """
    Function to export the descriptions to a file
    """
    with open(output_file, "w", encoding='utf-8-sig') as file:
        for description in descriptions:
            print(description, file=file)


if __name__ == "__main__":
    split_corpus(input_file="./data/ecom-train.csv")
    corpus_to_test(input_file="./data/ecom-train.csv")
