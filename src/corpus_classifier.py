#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: corpus_classifier.py
Author: Sergio Tabares Hernández <alu0101124896@ull.edu.es>
Since: Sprint 2021
College: University of La Laguna
Degree: Computer Science - Advanced Artificial Intelligence
Description: This program classifies the test corpus into the learned classes
"""

from src.data_getters import raw_descriptions_data, vocabulary_data, classes_data
from src.data_getters import real_document_classes_data, class_probabilities_data
from src.data_getters import classified_document_classes_data, test_corpus_data


def classify_corpus(vocabulary=None,
                    classes=None,
                    test_corpus=None,
                    output_to_file=False):
    """
    Function to classify the test corpus documents into the learned classes
    """
    # studentCode = input("Código de alumno: ")

    print("Classifying documents (this could take some time)...")

    if vocabulary is None:
        vocabulary_size, vocabulary = vocabulary_data()
    else:
        vocabulary_size = len(vocabulary)

    if classes is None:
        _, classes = classes_data()

    if test_corpus is None:
        test_corpus_size, test_corpus, test_corpus_file = test_corpus_data()
        raw_descriptions = raw_descriptions_data(input_file=test_corpus_file)
    else:
        test_corpus_size = len(test_corpus)

    results = {
        documentId: {
            "description": test_corpus[documentId],
            "classLogProbs": []
        }
        for documentId in range(test_corpus_size)
    }

    probabilities_data = {
        className: class_probabilities_data(className)
        for className in classes
    }

    for class_data in probabilities_data.values():
        if vocabulary_size != len(class_data.get("classProbabilities")):
            raise ValueError(
                "The vocabulary doesn't correspond to the class probabilities")

    for document_id in range(test_corpus_size):
        for class_data in probabilities_data.values():
            documents_in_class_corpus, _, class_probabilities = class_data.values(
            )

            current_document_words_log_probs = [
                class_probabilities.get(word).get("logProb")
                for word in results.get(document_id).get("description")
            ]

            class_log_probs = documents_in_class_corpus / test_corpus_size
            current_document_log_prob = sum(current_document_words_log_probs,
                                            class_log_probs)

            results.get(document_id).get("classLogProbs").append(
                current_document_log_prob)

        best_document_log_prob = max(
            results.get(document_id).get("classLogProbs"))
        best_class_index = results.get(document_id).get("classLogProbs").index(
            best_document_log_prob)

        results.get(document_id).update(
            {"bestClass": classes[best_class_index][0]})

    if output_to_file:
        print("Exporting to files...")
        # exportToFile(results, rawDescriptions, studentCode)
        export_to_file(results, raw_descriptions)

    return results


def check_precision(original_file="./data/ecom-train.csv",
                    classified_file="./data/resumen-train.csv"):
    """
    Function to check the precision on the classified descriptions
    """
    print("Checking precision...")

    real_classes = real_document_classes_data(original_file)
    results_list = classified_document_classes_data(classified_file)

    guessed_classes = list(
        map(lambda result, real: result[-1] == real, results_list,
            real_classes))

    num_of_guessed_documents = len(guessed_classes) - guessed_classes.count(
        False)
    success_rate = num_of_guessed_documents * 100 / len(guessed_classes)

    print(num_of_guessed_documents, "of", len(guessed_classes))
    print("Success rate:", str(success_rate) + "%")


def export_to_file(results, raw_descriptions, student_code=None):
    """
    Function to export the classified descriptions to a file
    """
    # classifyOutputFile = "./data/clasificacion-alu0101124896.csv"
    # resumeOutputFile = "./data/resumen-alu0101124896.csv"
    classify_output_file = "./data/clasificacion-train.csv"
    resume_output_file = "./data/resumen-train.csv"

    with open(classify_output_file, "w", encoding='utf-8-sig') as c_file:
        with open(resume_output_file, "w", encoding='utf-8-sig') as r_file:
            if student_code is not None:
                print(f"Código: {student_code}", file=r_file)

            for document_index, classified_document in enumerate(
                    results.values()):
                print(raw_descriptions[document_index], end=",", file=c_file)

                for class_log_prob in classified_document.get("classLogProbs"):
                    print(round(class_log_prob, 2), end=",", file=c_file)

                print(classified_document.get("bestClass"), file=c_file)
                print(classified_document.get("bestClass"), file=r_file)


if __name__ == "__main__":
    classify_corpus()
    check_precision()

    # classifyCorpus(inputFile="./data/ecom-test.csv")
    # checkPrecision(originalFile="./data/ecom-test-check-20.csv",
    #                classifiedFile="./data/resumen-alu0101124896.csv")
