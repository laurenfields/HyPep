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


#simp_mass_db = pd.DataFrame(mass_sequence) #making dataframe for mass database
simp_query = pd.DataFrame(mass_q_sequence) #dataframe for query

monoiso['Monoisotopic Mass'] = monoiso['Monoisotopic Mass'].apply(pd.to_numeric)
simp_query['Mass'] = simp_query['Mass'].apply(pd.to_numeric)
tolerance = tol_in #provides margin of error
match_mass = lambda x: np.any(np.isclose(x, simp_query['Mass'], atol=tolerance))
monoiso['masses match'] = monoiso['Monoisotopic Mass'].apply(match_mass)
monoiso = monoiso[monoiso['masses match'] == True] #remove all false rows from table
