# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:25:21 2021

@author: lawashburn
"""

from User_input import sequence
import pandas as pd


seq = pd.DataFrame(sequence)
seq = seq.astype(str) # changes all mass values out for strings for replacement to happen


seq = seq.replace('A','1')
seq = seq.replace('R','1')
seq = seq.replace('N','1')
seq = seq.replace('D','1')
seq = seq.replace('C','1')
seq = seq.replace('E','1')
seq = seq.replace('Q','1')
seq = seq.replace('G','1')
seq = seq.replace('H','1')
seq = seq.replace('O','1')
seq = seq.replace('I','1')
seq = seq.replace('L','1')
seq = seq.replace('K','1')
seq = seq.replace('M','1')
seq = seq.replace('F','1')
seq = seq.replace('P','1')
seq = seq.replace('S','1')
seq = seq.replace('T','1')
seq = seq.replace('W','1')
seq = seq.replace('Y','1')
seq = seq.replace('V','1')

seq= seq.apply(pd.to_numeric, errors='ignore')

seq['Sum'] = seq.sum(axis =1)

mass_sub = pd.DataFrame()
mass_sub['len'] = seq['Sum']
mass_sub['mod_len'] = mass_sub['len'] - 1
mass_sub['prelim'] = mass_sub['mod_len'] * 18
mass_sub['subtract'] = mass_sub['prelim'] + 18

subtract = pd.DataFrame()
subtract['subtract'] = mass_sub['subtract']
