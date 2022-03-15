#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: probabilities_estimator.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Sprint 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program estimates the probability values of every word in
  the vocabulary for each class corpus
"""

import math

from src.data_getters import classes_data, class_corpus_data, vocabulary_data


def estimate_probabilities(vocabulary=None,
                           classes=None,
                           splitted_corpus=None,
                           output_to_file=False):
    """
    Main function to estimate the probability values of every word in the
      vocabulary for each class corpus
    """
    if vocabulary is None:
        vocabulary_size, vocabulary = vocabulary_data()
    else:
        vocabulary_size = len(vocabulary)

    if classes is None:
        _, classes = classes_data()

    k_unk = 0  # unknown word umbral value
    probabilities_data = dict()

    for class_name in classes:
        print(f"Estimating {class_name} class probabilities...")

        documents_in_class_corpus, words_in_class_corpus, class_corpus_words = \
            class_corpus_data(class_name, splitted_corpus)

        word_frequencies = {word: 0 for word in vocabulary}

        for word in class_corpus_words:
            current_word_frequency = word_frequencies.get(word)

            if current_word_frequency is None:
                word_frequencies.update({word: 1})
            else:
                word_frequencies.update({word: current_word_frequency + 1})

        class_probabilities = {
            word: {
                "freq":
                frequency,
                "logProb":
                math.log(
                    (frequency + 1) / (words_in_class_corpus + vocabulary_size))
            } if frequency > k_unk else {
                "freq":
                0,
                "logProb":
                math.log((0 + 1) / (words_in_class_corpus + vocabulary_size))
            }
            for word, frequency in word_frequencies.items()
        }

        if vocabulary[-1] == "<unk>":
            class_probabilities.update({
                "<unk>": {
                    "freq":
                    k_unk,
                    "logProb":
                    math.log(
                        (k_unk + 1) / (words_in_class_corpus + vocabulary_size))
                }
            })

        probabilities_data.update({
            class_name: {
                "documentsInClassCorpus": documents_in_class_corpus,
                "wordsInClassCorpus": words_in_class_corpus,
                "classProbabilities": class_probabilities
            }
        })

    if output_to_file:
        print("Exporting probabilities to files...")
        for class_name, class_data in probabilities_data.items():
            documents_in_class_corpus, words_in_class_corpus, class_probabilities = \
              class_data.values()
            export_to_file(class_name, documents_in_class_corpus,
                           words_in_class_corpus, class_probabilities)

    return probabilities_data


def export_to_file(class_name, documents_in_class_corpus, words_in_class_corpus,
                   class_probabilities):
    """
    Function to export the class probabilities to a file
    """
    # output_file = input(f"{class_name} learned probabilities output file " +
    #                     f"(Default = ./data/aprendizaje{class_name[0]}.txt):"
    #                     ) or f"./data/aprendizaje{class_name[0]}.txt"
    output_file = f"./data/aprendizaje{class_name[0]}.txt"

    with open(output_file, "w", encoding='utf-8-sig') as file:
        print(f"Numero de documentos del corpus: {documents_in_class_corpus}",
              file=file)
        print(f"Numero de palabras del corpus: {words_in_class_corpus}",
              file=file)

        for word, data in class_probabilities.items():
            print(f"Palabra: {word}",
                  f"Frec: {data.get('freq')}",
                  f"LogProb: {data.get('logProb')}",
                  file=file)


if __name__ == "__main__":
    estimate_probabilities()
