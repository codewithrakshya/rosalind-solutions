#!/usr/bin/env python3
#BME205
#Rakshya Sharma

from Problem20 import OutcomeCalculator
"""
Outcome Likelihood Problem

Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The probability Pr(x) that the HMM emits x.
"""
class ViterbiAlgorithm:
    def __init__(self, file_path):
        self.sequence, self.states, self.transition_matrix, self.emission_matrix = self.read_file(file_path)

    def read_file(self, file_path):
        with open(file_path, 'r') as file:
            parts = file.read().split('--------')
            sequence = parts[0].strip()
            alphabet = parts[1].strip().split()
            states = parts[2].strip().split()

            transition_lines = parts[3].strip().split('\n')[1:]
            transition_matrix = {}
            for line in transition_lines:
                elements = line.split()
                transition_matrix[elements[0]] = {state: float(prob) for state, prob in zip(states, elements[1:])}

            emission_lines = parts[4].strip().split('\n')[1:]
            emission_matrix = {}
            for line in emission_lines:
                elements = line.split()
                emission_matrix[elements[0]] = {symbol: float(prob) for symbol, prob in zip(alphabet, elements[1:])}

            return sequence, states, transition_matrix, emission_matrix


    def viterbi(self):
        len_seq = len(self.sequence)
        len_states = len(self.states)
        viterbi_matrix = [[0 for _ in range(len_seq)] for _ in range(len_states)]
        backpointer = [[0 for _ in range(len_seq)] for _ in range(len_states)]

        for s in range(len_states):
            viterbi_matrix[s][0] = 1.0 / len_states * self.emission_matrix[self.states[s]][self.sequence[0]]
            backpointer[s][0] = 0

        for t in range(1, len_seq):
            for s in range(len_states):
                max_prob = -1
                for s_prev in range(len_states):
                    prob = viterbi_matrix[s_prev][t-1] * self.transition_matrix[self.states[s_prev]][self.states[s]] * self.emission_matrix[self.states[s]][self.sequence[t]]
                    if prob > max_prob:
                        max_prob = prob
                        backpointer[s][t] = s_prev
                viterbi_matrix[s][t] = max_prob

        last_probs = [viterbi_matrix[s][-1] for s in range(len_states)]
        best_last_state = last_probs.index(max(last_probs))

        best_path = [self.states[best_last_state]]
        for t in range(len_seq - 1, 0, -1):
            best_last_state = backpointer[best_last_state][t]
            best_path.insert(0, self.states[best_last_state])

        return ''.join(best_path)

file_path = 'rosalind_ba10c.txt'
viterbi = ViterbiAlgorithm(file_path)
best_path = viterbi.viterbi()
print(f"Problem 21.py : {best_path}")