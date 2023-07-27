class complement:
    def reverse(self):
        return self[::-1]
    def complement_dna(self):
         complement = {'A':'T', 'T':'A','C':'G','G':'C'}
         complemented_seq = ''.join(complement[base]for base in self)
         return complemented_seq
    def reverse_complement(self):
        reversed_seq = complement.reverse(self)
        return complement.complement_dna(reversed_seq)
filepath = "/workspaces/rosalind-solutions/Complementing_a_Strand_of_DNA/rosalind_revc-2.txt"
counter = complement()

with open(filepath, "r") as file:
    sequence = file.read().strip()

reversed_complemented_seq = complement.reverse_complement(sequence)

print(reversed_complemented_seq)
