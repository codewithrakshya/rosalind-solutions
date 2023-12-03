#!/usr/bin/env python3
#BME205
#Rakshya Sharma

from Problem19 import HiddenPath
"""
Probability of an Outcome Given a Hidden Path Problem

Given: A string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π.
"""

class OutcomeCalculator:
    def __init__(self, infile):
        self.infile = infile

    def read_data(self):
        try:
            with open(self.infile, 'r') as file:
                data = file.read().split()
                sequence = data[0]
                path = data[6]
                emission_matrix = {
                    'A': {'x': float(data[-7]), 'y': float(data[-6]), 'z': float(data[-5])},
                    'B': {'x': float(data[-3]), 'y': float(data[-2]), 'z': float(data[-1])}
                }
                return sequence, path, emission_matrix
        except FileNotFoundError:
            print(f"File {self.infile} not found.")
            return None, None, None

    def calculate_probability(self, sequence, path, emission_matrix):
        probability = 1
        for i in range(len(sequence)):
            probability *= emission_matrix[path[i]][sequence[i]]
        return probability

    def run(self):
        sequence, path, emission_matrix = self.read_data()
        if sequence and path and emission_matrix:
            # You can use HiddenPath or its methods here if needed
            prob = self.calculate_probability(sequence, path, emission_matrix)
            print(f"Problem20.py : {prob}")

if __name__ == '__main__':
    calculator = OutcomeCalculator('rosalind_ba10b.txt')
    calculator.run()
