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

class Substring:
    def __init__(self, dna):
        self.dna = dna

    def dna_to_rna(self):
        return self.dna.replace('T', 'U')
    
    def reverse_comp(self):
        complement = ''
        for nucleotide in self.dna:
            if nucleotide == 'A':
                complement += 'T'
            elif nucleotide == 'T':
                complement += 'A'
            elif nucleotide == 'C':
                complement += 'G'
            elif nucleotide == 'G':
                complement += 'C'
        return complement[::-1]
    
    def translate_rna(rna):
        integerMass = { 'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186 }

        dnaCodonTable = {
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
