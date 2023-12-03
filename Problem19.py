#!/usr/bin/env python3
#BME205
#Rakshya Sharma

"""
Probability of a Hidden Path Problem

Given: A hidden path π followed by the states States and transition matrix Transition of an HMM (Σ, States, Transition, Emission).

Return: The probability of this path, Pr(π). You may assume that initial probabilities are equal.
"""
class HiddenPath:
    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.path = file.readline().strip()
            file.readline()  # Skip the '--------' line

            states = file.readline().strip().split()
            self.transition_matrix = {state: {} for state in states}

            file.readline()  # Skip the '--------' line
            states_column = file.readline().strip().split()

            for line in file:
                parts = line.strip().split()
                state_from = parts[0]
                for i, state_to in enumerate(states_column):
                    self.transition_matrix[state_from][state_to] = float(parts[i + 1])

    def calculate_path_probability(self):
        probability = 1.0 / len(self.transition_matrix)

        for i in range(len(self.path) - 1):
            probability *= self.transition_matrix[self.path[i]][self.path[i + 1]]

        return probability


if __name__ == '__main__':
    file_path = 'rosalind_ba10a.txt'
    hidden_path_obj = HiddenPath(file_path)
    probability = hidden_path_obj.calculate_path_probability()
    print(f"Problem19.py : {probability}")
