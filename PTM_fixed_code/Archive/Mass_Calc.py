# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:34:02 2021

@author: lawashburn
"""

aminoacid = {
    'I': 'C6H13NO2',
    'L': 'C6H13NO2',
    'K': 'C6H14N2O2',
    'M': 'C5H11NO2S',
    'F': 'C9H11NO2',
    'T': 'C4H9NO3',
    'W': 'C11H12N2O2',
    'V': 'C5H11NO2',
    'R': 'C6H14N4O2',
    'H': 'C6H9N3O2',
    'A': 'C3H7NO2',
    'N': 'C4H8N2O3',
    'D': 'C4H7NO4',
    'C': 'C3H7NO2S',
    'E': 'C5H9NO4',
    'Q': 'C5H10N2O3',
    'G': 'C2H5NO2',
    'P': 'C5H9NO2',
    'S': 'C3H7NO3',
    'Y': 'C9H11NO3'
}
monoisotopic = {
    'S': 31.972,
    'C': 12.0000,
    'H': 1.0078,
    'O': 15.9949,
    'N': 14.0031
}

from re import findall as refindall

def molecular_weight(molecule):
    return sum(
        monoisotopic[atom] * int(num or '1')
        for atom, num in refindall(r'([A-Z][a-z]*)(\d*)', molecule)
    )

def protein_mass(protein):
    return sum(molecular_weight(aminoacid[char]) for char in protein)

seq = [('KGTLPK'),('KTGPLK'),('GGTKKP')]

for a in seq:
    mass = protein_mass(a)
    print(mass)