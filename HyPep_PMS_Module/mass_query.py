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
from User_input import ppm_err

df_seq2['mass_pos'] = df_seq2['mass_pos'].apply(pd.to_numeric) #experimental masses
mass_q_sequence['Mass'] = mass_q_sequence['Mass'].apply(pd.to_numeric) #tells pandas these are numbers

tolerance = tol_in #provides margin of error
match_mass = lambda x: np.any(np.isclose(x, mass_q_sequence['Mass'], atol=tolerance))
df_seq2['masses match'] = df_seq2['mass_pos'].apply(match_mass)

df_seq2 = df_seq2[df_seq2['masses match'] == True] #remove all false rows from table

mass_seq = mass_q_sequence['Mass'].values.tolist()
mass_pos = df_seq2['mass_pos'].values.tolist()

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

near_lst = []

for x in mass_pos:
    nearest=(find_nearest(mass_seq, x))
    near_lst.append(nearest)

error = pd.DataFrame()
error['possible masses'] = mass_pos
error['nearest exp'] = near_lst

error1 = error['possible masses']
error2 = error['nearest exp']
error['int_err_1'] = error1-error2
error3 = error['int_err_1']
error['int_err_2'] = error3 / error1
error4= error['int_err_2']
error['int_err_3'] = abs(error4)
error5 = error['int_err_3']
error['error'] = error5 * 1E6


df_seq2.reset_index(drop=True, inplace=True)

df_seq2['error'] = error['error']
df_seq2 = df_seq2[df_seq2.error <= ppm_err]
df_seq2 = df_seq2.drop('masses match', 1)
df_seq2 = df_seq2.drop('Precursor', 1)
print(df_seq2)

#for PTM reporting:
df_ptm_mass = pd.DataFrame()

df_ptm_mass['PTM Mass'] = df_seq2['mass']
df_ptm_mass = df_ptm_mass.values.tolist()


df_ptm_mass2 = list(chain.from_iterable(df_ptm_mass))
df_ptm_mass3 = list(set(df_ptm_mass2))

