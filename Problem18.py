#!/usr/bin/env python3
#BME205
#Rakshya Sharma
"""
In “Compute the Number of Peptides of Given Total Mass”, we first encountered the problem of reconstructing a cyclic peptide from its theoretical spectrum; this problem is called the Cyclopeptide Sequencing Problem and is given below. It is solved by the following algorithm.

    CYCLOPEPTIDESEQUENCING(Spectrum)
        Peptides ← a set containing only the empty peptide
        while Peptides is nonempty
            Peptides ← Expand(Peptides)
            for each peptide Peptide in Peptides
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Cyclospectrum(Peptide) = Spectrum
                        output Peptide
                    remove Peptide from Peptides
                else if Peptide is not consistent with Spectrum
                    remove Peptide from Peptides
Cyclopeptide Sequencing Problem
Given an ideal experimental spectrum, find a cyclic peptide whose theoretical spectrum matches the experimental spectrum.

Given: A collection of (possibly repeated) integers Spectrum corresponding to an ideal experimental spectrum.

Return: Every amino acid string Peptide such that Cyclospectrum(Peptide) = Spectrum (if such a string exists).

"""
class AminoAcidChain:
    def __init__(self, mass_table):
        self.mass_table = {
            'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101,
            'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128,
            'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
        }

    def generate_cyclic_spectrum(self, peptide):
        prefix_mass = [0]
        for i in range(len(peptide)):
            prefix_mass.append(prefix_mass[i] + self.mass_table[peptide[i]])

        full_mass = prefix_mass[-1]
        cyclic_spectrum = [0]
        for i in range(len(peptide)):
            for j in range(i + 1, len(peptide) + 1):
                mass = prefix_mass[j] - prefix_mass[i]
                cyclic_spectrum.append(mass)
                if i > 0 and j < len(peptide):
                    cyclic_spectrum.append(full_mass - mass)

        cyclic_spectrum.sort()
        return set(cyclic_spectrum)

    def build_peptides(self, current_peptides):
        new_peptides = set()
        for p in current_peptides:
            for aa in self.mass_table.keys():
                new_peptides.add(p + aa)
        return new_peptides

    def calculate_mass(self, peptide):
        return sum(self.mass_table[aa] for aa in peptide)

    def find_cyclic_peptides(self, experimental_spectrum):
        candidate_peptides = {''}
        while candidate_peptides:
            candidate_peptides = self.build_peptides(candidate_peptides)
            for peptide in candidate_peptides.copy():
                if self.calculate_mass(peptide) == max(experimental_spectrum):
                    if self.generate_cyclic_spectrum(peptide) == experimental_spectrum:
                        return peptide
                    else:
                        candidate_peptides.remove(peptide)

    def generate_combinations(self, peptide_masses):
        combinations = []
        for i in range(len(peptide_masses)):
            rotated = peptide_masses[i:] + peptide_masses[:i]
            combinations.append('-'.join(rotated))
        return combinations

def process_data(file_path):
    with open(file_path, 'r') as file:
        experimental_spectrum = set(map(int, file.readline().split()))

    amino_acid_chain = AminoAcidChain(mass_table={})
    identified_peptide = amino_acid_chain.find_cyclic_peptides(experimental_spectrum)

    peptide_masses = [str(amino_acid_chain.mass_table[aa]) for aa in identified_peptide]
    forward_combinations = amino_acid_chain.generate_combinations(peptide_masses)
    backward_combinations = amino_acid_chain.generate_combinations(peptide_masses[::-1])

    final_output = forward_combinations + backward_combinations
    with open('output.txt', 'w') as output_file:
        output_file.write(' '.join(final_output))

if __name__ == "__main__":
    process_data('rosalind_ba4e.txt')
