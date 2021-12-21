# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:53:01 2021

@author: lawashburn
"""

from User_input import sequence
from amt_subtract import subtract
import pandas as pd
import numpy as np

x = sequence.to_string(header=False,
                  index=False,
                  index_names=False).split('\n')
seq_vals = [''.join(ele.split()) for ele in x]

lst_seq2 = [e[1:] for e in seq_vals] #list
lst_seq = list(lst_seq2)



seq = pd.DataFrame(sequence)
seq = seq.astype(str) # changes all mass values out for strings for replacement to happen
seq['full seq'] = seq.values.sum(axis=1)

seq2 = pd.DataFrame()
seq2 = seq[seq.columns.difference(["full seq"])]

seq = seq.drop(seq2, axis=1)

print(seq)