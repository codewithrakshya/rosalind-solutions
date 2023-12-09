#!/usr/bin/env python3
#BME205
#Rakshya Sharma
"""
There are three different ways to divide a DNA string into codons for translation, one starting at each of the first three starting positions of the string. These different ways of dividing a DNA string into codons are called reading frames. Since DNA is double-stranded, a genome has six reading frames (three on each strand), as shown in Figure 1.

We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide.

Peptide Encoding Problem
Find substrings of a genome encoding a given amino acid sequence.

Given: A DNA string Text and an amino acid string Peptide.

Return: All substrings of Text encoding Peptide (if any such substrings exist).
"""
class PeptideEncoder:
    """
    This class stores a DNA sequence, its corresponding amino acid sequence, and a codon table 
    """
    def __init__(self, dna_sequence, amino_acid_sequence):
        self.dna_sequence = dna_sequence
        self.amino_acid_sequence = amino_acid_sequence
        self.codon_table = {
        # T
        'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C', 
        'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C', 
        'TTA': 'L', 'TCA': 'S', 'TAA': 'STOP', 'TGA': 'STOP',
        'TTG': 'L', 'TCG': 'S', 'TAG': 'STOP', 'TGG': 'W', 
        # A
        'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S', 
        'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', 
        'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', 
        'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', 
        # C
        'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R', 
        'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', 
        'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 
        'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
        # G
        'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G', 
        'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
        'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
        'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
    }
    def get_reverse_complement(self, sequence):
        '''
        Generating the reverse complement of a DNA sequence, maps each nucleotide to its complement and reverses the string
        to generate the reverse complement
        '''
        base_pair = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return ''.join(base_pair[base] for base in reversed(sequence))
    
    def to_peptide(self, dna_segment):
        '''
        Converting a DNA segment to its corresponding peptide sequence, trans;ates the DNA segement into a peptide sequence using the
        codon table and Stopping at STOP codon
        '''
        peptide = ''
        for i in range(0, len(dna_segment), 3):
            codon = dna_segment[i:i+3]
            amino_acid = self.codon_table.get(codon)
            if amino_acid == 'STOP':
                break
            peptide += amino_acid
        return peptide
    
    def find_encoding_substrings(self):
        '''
        Identifying substrings of the DNA sequence that encode the given amino acid sequence.
        This scans the DNA sequnce and its reverse complement, translating each segment into a peptide and checking if it
        matched the target amino acid sequence
        '''
        encoded_substrings = []
        segment_length = len(self.amino_acid_sequence) * 3
        for i in range(len(self.dna_sequence) - segment_length + 1):
            segment = self.dna_sequence[i:i+segment_length]
            peptide = self.to_peptide(segment)
            reverse_peptide = self.to_peptide(self.get_reverse_complement(segment))
            if peptide == self.amino_acid_sequence or reverse_peptide == self.amino_acid_sequence:
                encoded_substrings.append(segment)
        return encoded_substrings
    
def main(input_file=None):
    with open(input_file, 'r') as file:
        dna_sequence = file.readline().strip()
        amino_acid_sequence = file.readline().strip()

    encoder = PeptideEncoder(dna_sequence, amino_acid_sequence)
    result = encoder.find_encoding_substrings()
    
    for substring in result:
        print(substring)

if __name__ == "__main__":
    main(input_file='rosalind_ba4b.txt')
