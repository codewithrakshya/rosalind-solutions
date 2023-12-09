#!/usr/bin/env python3
#BME205
#Rakshya Sharma
"""
The workhorse of peptide sequencing is the mass spectrometer, an expensive molecular scale that shatters molecules into pieces and then weighs the resulting fragments. The mass spectrometer measures the mass of a molecule in daltons (Da); 1 Da is approximately equal to the mass of a single nuclear particle (i.e., a proton or neutron).

We will approximate the mass of a molecule by simply adding the number of protons and neutrons found in the molecule’s constituent atoms, which yields the molecule’s integer mass. For example, the amino acid "Gly", which has chemical formula C2H3ON, has an integer mass of 57, since 2·12 + 3·1 + 1·16 + 1·14 = 57. Yet 1 Da is not exactly equal to the mass of a proton/neutron, and we may need to account for different naturally occurring isotopes of each atom when weighing a molecule. As a result, amino acids typically have non-integer masses (e.g., "Gly" has total mass equal to approximately 57.02 Da); for simplicity, however, we will work with the integer mass table given in Figure 1.

The theoretical spectrum of a cyclic peptide Peptide, denoted Cyclospectrum(Peptide), is the collection of all of the masses of its subpeptides, in addition to the mass 0 and the mass of the entire peptide. We will assume that the theoretical spectrum can contain duplicate elements, as is the case for "NQEL" (shown in Figure 2), where "NQ" and "EL" have the same mass.

Generating Theoretical Spectrum Problem
Generate the theoretical spectrum of a cyclic peptide.

Given: An amino acid string Peptide.

Return: Cyclospectrum(Peptide).
"""

class CyclicPeptide:
    """
    This class takes a peptide sequence as input and provides a method to calculate
    the theoretical mass spectrum of the cyclic form of the peptide. It uses an
    internal dictionary to map amino acids to their respective integer masses.

    """
    def __init__(self, peptide_sequence):
        self.peptide_sequence = peptide_sequence
        self.amino_acid_masses = {
                    'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 
                    'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128,
                    'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186
                    }
    
    def generate_cyclic_spectrum(self):
        """
        This method is generating the theoretical spectrum of a cyclic peptide and returns list of integers representing the Cyclospectrum of the peptide.
        """
        prefix_masses = [0]
        for amino_acid in self.peptide_sequence:
            prefix_masses.append(prefix_masses[-1] + self.amino_acid_masses[amino_acid])

        peptide_mass = prefix_masses[-1]
        cyclic_spectrum = [0]
        
        for i in range(len(self.peptide_sequence)):
            for j in range(i + 1, len(self.peptide_sequence) + 1):
                mass = prefix_masses[j] - prefix_masses[i]
                cyclic_spectrum.append(mass)
                if i > 0 and j < len(self.peptide_sequence):
                    cyclic_spectrum.append(peptide_mass - mass)

        cyclic_spectrum.sort()
        return cyclic_spectrum

def main(input_file=None):
    with open(input_file, 'r') as file:
        peptide_sequence = file.readline().strip()

    cyclic_peptide = CyclicPeptide(peptide_sequence)
    spectrum = cyclic_peptide.generate_cyclic_spectrum()

    print(' '.join(map(str, spectrum)))

if __name__ == "__main__":
    main(input_file='rosalind_ba4c.txt')