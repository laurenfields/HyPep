# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:53:43 2021

@author: lawashburn
"""
#Finds all matches between query and database masses within a given margin

import numpy as np
import pandas as pd
from Database_Split import df_seq
from itertools import chain
from User_input import mass_q_sequence
from User_input import tol_in


df_seq['mass_pos'] = df_seq['mass_pos'].apply(pd.to_numeric) #experimental masses
mass_q_sequence['Mass'] = mass_q_sequence['Mass'].apply(pd.to_numeric) #tells pandas these are numbers

tolerance = tol_in #provides margin of error
match_mass = lambda x: np.any(np.isclose(x, mass_q_sequence['Mass'], atol=tolerance))
df_seq['masses match'] = df_seq['mass_pos'].apply(match_mass)
df_seq = df_seq[df_seq['masses match'] == True] #remove all false rows from table

df_ptm_mass = pd.DataFrame()

df_ptm_mass['PTM Mass'] = df_seq['mass']
print('df ptm mass equals',df_ptm_mass)

df_ptm_mass = df_ptm_mass.values.tolist()


df_ptm_mass2 = list(chain.from_iterable(df_ptm_mass))
df_ptm_mass3 = list(set(df_ptm_mass2))

