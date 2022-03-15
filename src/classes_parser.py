#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: classes_parser.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Sprint 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program obtains the classes of the given descriptions,
 in this case, the first column of the given csv file.
"""

from src.corpus_parser import extract_classes
from src.data_getters import get_raw_data


def parse_classes(input_file, output_to_file=False):
    """
    Main function to obtain the classes form the given csv file
    """
    print("Parsing classes...")

    # corpus_raw_data = get_raw_data(input_file)
    # classes = list(extract_classes(corpus_raw_data))
    # classes.sort()

    # required in the next order for the classification output file format:
    classes = ["Household", "Books", "Clothing & Accessories", "Electronics"]

    if output_to_file:
        # output_file = input("Classes output file (Default = ./data/clases.txt):"
        #                    ) or "./data/clases.txt"
        output_file = "./data/clases.txt"

        export_to_file(classes, output_file)

    return classes


def export_to_file(classes, output_file):
    """
    Function to export the classes to a file
    """
    with open(output_file, "w", encoding='utf-8-sig') as file:
        print(f"Numero de clases: {len(classes)}", file=file)

        for class_name in classes:
            print(class_name, file=file)


if __name__ == "__main__":
    parse_classes(input_file="./data/ecom-train.csv")
