#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: data_getters_test.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Autumn 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program tests the correct functionality of the functions at
 src/dataGetters.py file.
"""

import unittest

from src.data_getters import get_raw_data, vocabulary_data, classes_data
from src.data_getters import raw_descriptions_data, real_document_classes_data
from src.data_getters import classified_document_classes_data


class DataGettersTestCase(unittest.TestCase):
    """
    Class to test the data_getters script.
    """
    def test_get_raw_data(self):
        """
        Function to test the get_raw_data function.
        """
        corpus_raw_data = get_raw_data("./test/data/corpus.csv")
        result = [
            "FirstClass,This is the description of something",
            "SecondClass,This description tests the program",
            "ThirdClass,This is another description for the tests"
        ]

        self.assertEqual(corpus_raw_data, result)

    def test_vocabulary_data(self):
        """
        Function to test the test_vocabulary_data function.
        """
        vocabulary_size, vocabulary = vocabulary_data(
            "./test/data/vocabulario.txt")
        result = [
            "another",
            "description",
            "program",
            "something",
            "tests",
            "<unk>",
        ]

        self.assertEqual(vocabulary, result)
        self.assertEqual(vocabulary_size, len(result))

    def test_classes_data(self):
        """
        Function to test the test_classes_data function.
        """
        num_of_classes, classes = classes_data("./test/data/classes.txt")
        result = ["FirstClass", "SecondClass", "ThirdClass"]

        self.assertEqual(classes, result)
        self.assertEqual(num_of_classes, len(result))

    def test_raw_descriptions_data(self):
        """
        Function to test the test_raw_descriptions_data function.
        """
        descriptions = raw_descriptions_data("./test/data/corpus.csv")
        result = [
            "This is the description of something",
            "This description tests the program",
            "This is another description for the tests"
        ]

        self.assertEqual(descriptions, result)

    def test_real_document_classes_data(self):
        """
        Function to test the test_real_document_classes_data function.
        """
        classes = real_document_classes_data("./test/data/corpus.csv")
        result = ["F", "S", "T"]

        self.assertEqual(classes, result)

    def test_classified_document_classes_data(self):
        """
        Function to test the test_classified_document_classes_data function.
        """
        classes = classified_document_classes_data("./test/data/resumen.csv")
        result = ["F", "S", "T"]

        self.assertEqual(classes, result)


if __name__ == "__main__":
    unittest.main()
