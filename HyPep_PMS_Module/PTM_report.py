# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:20:49 2021

@author: lawashburn
"""


import pandas as pd
import itertools
import numpy as np
from mass_query import df_ptm_mass3

numbers = [-1,0,1,14,16,17,22,28,31,32,40,42,43,44,46,47,59,58,68,70,71,80,87,99,
           100,105,114,125,162,203,210,226] #possible mass outcomes, see excel file in package for full list of mods

for a in df_ptm_mass3: #calls each PTM mass identified

    target = a

    result = [seq for i in range(len(numbers), 0, -1) #finds what iterations of PTM masses equal value of PTM mass identified
              for seq in itertools.combinations(numbers, i)
              if sum(seq) == target]

    df = pd.DataFrame(result) #puts result in a dataframe
    df.dropna(thresh=2)
    df = df.replace(np.nan, 0)
    df = df.astype(int) #makes all mass values ints
    df = df.astype(str) # changes all mass values out for strings for replacement to happen
    
    #Replaces all masses with the PTM they represent
    
    df = df.replace('-1','Amidation')
    df = df.replace('1', 'Deamidation')
    df = df.replace('14', 'Methylation')
    df = df.replace('16', 'Hydroxylation or Oxidation')
    df = df.replace('17', 'Glu to PyroGlu')
    df = df.replace('22', 'Sodium Adduct')
    df = df.replace('28', 'Formylation or Dimethylation')
    df = df.replace('31', 'Citrullination')
    df = df.replace('32', 'Dihydroxy')
    df = df.replace('40', 'S-carbamoylmethylcysteine cyclization')
    df = df.replace('42', 'Acetylation or Trimethylation')
    df = df.replace('43', 'Carbamylation')
    df = df.replace('44', 'Carboxylation or Ethanolation')
    df = df.replace('46', 'Beta methylthiolation')
    df = df.replace('47', 'Nitrosylation')
    df = df.replace('57', 'Iodoacetamide derivative')
    df = df.replace('58','Iodoacetic acid derivative')
    df = df.replace('68','Crotonylation')
    df = df.replace('70', 'Butyrylation')
    df = df.replace('71', 'Lactylation or Acrylamide adduct')
    df = df.replace('80', 'Phosphorylation or sulfonation')
    df = df.replace('87', 'Hydroxybutyrylation')
    df = df.replace('99', 'N-isopropylcarboxamidomethyl')
    df = df.replace('100', 'Succinylation')
    df = df.replace('105', 'S-pyridylethyation')
    df = df.replace('114', 'Glutarylation')
    df = df.replace('125', 'Malonylation')
    df = df.replace('162', 'Hexose')
    df = df.replace('203', 'N-Acetylhexosamine')
    df = df.replace('210', 'Myristoylation')
    df = df.replace('226', 'Biotinylation')    
    df['target mass'] = target
    
    ptm_report_df = df
