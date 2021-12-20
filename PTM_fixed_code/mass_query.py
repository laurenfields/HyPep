# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 13:11:49 2021

@author: lawashburn
"""

#Finds all matches between query and database masses within a given margin

import numpy as np
import pandas as pd
from Database_Split import df_seq2
from itertools import chain
from User_input import mass_q_sequence
from User_input import tol_in



df_seq2['mass_pos'] = df_seq2['mass_pos'].apply(pd.to_numeric) #experimental masses
mass_q_sequence['Mass'] = mass_q_sequence['Mass'].apply(pd.to_numeric) #tells pandas these are numbers

tolerance = tol_in #provides margin of error
match_mass = lambda x: np.any(np.isclose(x, mass_q_sequence['Mass'], atol=tolerance))
df_seq2['masses match'] = df_seq2['mass_pos'].apply(match_mass)
df_seq2 = df_seq2[df_seq2['masses match'] == True] #remove all false rows from table
print('df_seq2 from mass_query',df_seq2)
#for PTM reporting:
df_ptm_mass = pd.DataFrame()

df_ptm_mass['PTM Mass'] = df_seq2['mass']
df_ptm_mass = df_ptm_mass.values.tolist()


df_ptm_mass2 = list(chain.from_iterable(df_ptm_mass))
df_ptm_mass3 = list(set(df_ptm_mass2))

