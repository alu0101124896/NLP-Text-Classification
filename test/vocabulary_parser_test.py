#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: vocabulary_parser_test.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Autumn 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program tests the correct functionality of the functions at
 src/vocabularyParser.py.
"""

import unittest

from src.vocabulary_parser import \
    parse_vocabulary, extract_vocabulary, export_to_file


class VocabularyParserTestCase(unittest.TestCase):
    """
    Class to test the vocabulary_parser script.
    """
    def test_extract_vocabulary(self):
        """
        Function to test the test_extract_vocabulary function.
        """
        vocabulary = extract_vocabulary([
            "This is the description of something",
            "This description tests the program",
            "This is another description for the tests",
        ])
        result = [
            "another",
            "description",
            "program",
            "something",
            "tests",
        ]
        self.assertEqual(vocabulary, result)

    def test_parse_vocabulary(self):
        """
        Function to test the test_parse_vocabulary function.
        """
        vocabulary = parse_vocabulary("./test/data/corpus.csv",
                                      output_to_file=True,
                                      output_file="./test/data/vocabulario.txt")
        result = [
            "another",
            "description",
            "program",
            "something",
            "tests",
            "<unk>",
        ]
        self.assertEqual(vocabulary, result)

        with open("./test/data/vocabulario.expected.txt",
                  "r",
                  encoding="utf-8-sig") as expected_file:
            with open("./test/data/vocabulario.txt", "r",
                      encoding="utf-8-sig") as result_file:
                self.assertEqual(expected_file.read(), result_file.read())

    # def test_export_to_file(self):
    #     """
    #     Function to test the test_export_to_file function.
    #     """


if __name__ == "__main__":
    unittest.main()
