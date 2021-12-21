# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 13:09:06 2021

@author: lawashburn
"""

from User_input2 import lst_seq
#from PTM_sample_4 import query
import pandas as pd
import numpy as np
#from PTM_sample_4 import combos_comb_sum_list
from PTM_sample_4 import all_combos

temp_df = pd.DataFrame()

sequence_with_combinations = []
while len(lst_seq) > 0:
    query_sequence = lst_seq[0]
    corresponding_query_ptm_comb = all_combos[0] 
    for c in corresponding_query_ptm_comb:
        sequence_with_combinations.append([query_sequence,c])
    lst_seq.remove(lst_seq[0])
    all_combos.remove(all_combos[0])

New_df = pd.DataFrame(np.array(sequence_with_combinations),columns=['entry','mass'])
temp_df = temp_df.append(New_df, ignore_index=True)
