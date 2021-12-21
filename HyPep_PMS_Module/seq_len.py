# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:05:19 2021

@author: lawashburn
"""

from User_input import sequence
import pandas as pd

seq = pd.DataFrame(sequence)

seq2 = seq.values.tolist()

seq2 = list(seq2)

for x in seq2:
    seq_len = len(x)
    print(seq_len)

mass_sub = pd.DataFrame()
mass_sub['seq_len'] = seq_len

print(mass_sub)