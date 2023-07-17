"""
https://rosalind.info/problems/rna/
"""

def T_to_U(sequence):
    return sequence.replace("T", "U")

filepath = "/workspaces/rosalind-solutions/Transcribing_DNA_into_RNA/rosalind_rna.txt"

with open(filepath, "r") as file:
    sequence = file.read()

modified_sequence = T_to_U(sequence)
print(modified_sequence)