# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:20:49 2021

@author: lawashburn
"""


import pandas as pd
import itertools
import numpy as np
from mass_query import df_ptm_mass3

numbers = [16,44,80,42,71,28,14,28,42,80,31,47,70,68,114,87,125,17] #possible mass outcomes

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
    
    df = df.replace('16','Hydroxylation')
    df = df.replace('44', 'Carboxylation')
    df = df.replace('80', 'Phosphorylation or Sulfonation')
    df = df.replace('42', 'Acetylation')
    df = df.replace('71', 'Lactylation')
    df = df.replace('28', 'Formylation or Dimethylation')
    df = df.replace('14', 'Methylation')
    df = df.replace('42', 'Trimethylation')
    df = df.replace('31', 'Citrullination')
    df = df.replace('47', 'Nitrosylation')
    df = df.replace('70', 'Butyrylation')
    df = df.replace('68', 'Crotonylation')
    df = df.replace('114', 'Glutarylation')
    df = df.replace('87', 'Hydroxybutyrylation')
    df = df.replace('125', 'Malonylation')
    df = df.replace('100', 'Succinylation')
    df = df.replace('17','Glu to PyroGlu')
    df['target mass'] = target
    
    ptm_report_df = df
