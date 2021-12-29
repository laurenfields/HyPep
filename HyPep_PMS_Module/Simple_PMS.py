# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 13:14:12 2021

@author: lawashburn
"""

#simple mass matching analysis

#import dataframe

from User_input import mass_q_sequence
from User_input2 import monoiso
import pandas as pd
from User_input import tol_in
import numpy as np
from Database_Split import df_seq2
from User_input import ppm_err


#simp_mass_db = pd.DataFrame(mass_sequence) #making dataframe for mass database
#simp_query = pd.DataFrame(mass_q_sequence) #dataframe for query

#monoiso['Monoisotopic Mass'] = monoiso['Monoisotopic Mass'].apply(pd.to_numeric)
#simp_query['Mass'] = simp_query['Mass'].apply(pd.to_numeric)
#tolerance = tol_in #provides margin of error
#match_mass = lambda x: np.any(np.isclose(x, simp_query['Mass'], atol=tolerance))
#monoiso['masses match'] = monoiso['Monoisotopic Mass'].apply(match_mass)
#monoiso = monoiso[monoiso['masses match'] == True] #remove all false rows from table
#print(monoiso)

monoiso = df_seq2
monoiso = monoiso.drop('mass',1)
monoiso = monoiso.drop('Precursor',1)
monoiso = monoiso.drop('mass_pos',1)


mass_seq = mass_q_sequence['Mass'].values.tolist()
mass_pos = monoiso['Monoisotopic'].values.tolist()

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

monoiso['error'] = error['error']

monoiso['error'] = pd.to_numeric(monoiso['error'], downcast='float')
monoiso = monoiso[monoiso.error <= ppm_err]
