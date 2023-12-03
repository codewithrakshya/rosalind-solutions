from Problem21 import ViterbiAlgorithm

class OutcomeLikelihood:
    def __init__(self, file_path):
        viterbi_algo = ViterbiAlgorithm(file_path)
        self.sequence = viterbi_algo.sequence
        self.states = viterbi_algo.states
        self.transition_matrix = viterbi_algo.transition_matrix
        self.emission_matrix = viterbi_algo.emission_matrix

    def forward_algorithm(self):
        len_seq = len(self.sequence)
        len_states = len(self.states)
        forward_matrix = [[0 for _ in range(len_seq)] for _ in range(len_states)]

        for s in range(len_states):
            forward_matrix[s][0] = 1.0 / len_states * self.emission_matrix[self.states[s]][self.sequence[0]]

        for t in range(1, len_seq):
            for s in range(len_states):
                forward_prob_s_t = 0.0
                for prev_s in range(len_states):
                    transition_prob = self.transition_matrix[self.states[prev_s]][self.states[s]]
                    emission_prob = self.emission_matrix[self.states[s]][self.sequence[t]]
                    prev_forward_prob = forward_matrix[prev_s][t-1]
                    forward_prob_s_t += prev_forward_prob * transition_prob * emission_prob

                forward_matrix[s][t] = forward_prob_s_t


        total_probability = sum(forward_matrix[s][-1] for s in range(len_states))

        return total_probability

file_path = 'rosalind_ba10d.txt'
outcome_likelihood = OutcomeLikelihood(file_path)
probability = outcome_likelihood.forward_algorithm()
print(f"Problem22.py : {probability}")