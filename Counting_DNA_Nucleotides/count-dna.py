class count_dna:
    def __init__(self):
        self.A = 0
        self.C = 0
        self.G = 0
        self.T = 0
    
    def count_sequence(self, sequence):
        self.A = sequence.count('A')
        self.C = sequence.count('C')
        self.G = sequence.count('G')
        self.T = sequence.count('T')

filepath = "/workspaces/rosalind-solutions/Counting_DNA_Nucleotides/rosalind_dna-3.txt"
counter = count_dna()

with open(filepath, "r") as file:
    sequence = file.read()

counter.count_sequence(sequence)

print(f"A: {counter.A}, C: {counter.C}, G: {counter.G}, T: {counter.T}")
