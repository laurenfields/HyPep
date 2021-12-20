# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 13:06:42 2021

@author: lawashburn
"""

from User_input import *
import pandas as pd
from amt_subtract import subtract


seq = pd.DataFrame(sequence)
seq = seq.astype(str) # changes all mass values out for strings for replacement to happen

seq = seq.replace('A','89.10')
seq = seq.replace('R','174.20')
seq = seq.replace('N','132.12')
seq = seq.replace('D','133.11')
seq = seq.replace('C','121.16')
seq = seq.replace('E','147.13')
seq = seq.replace('Q','146.15')
seq = seq.replace('G','75.07')
seq = seq.replace('H','155.16')
seq = seq.replace('O','131.13')
seq = seq.replace('I','131.18')
seq = seq.replace('L','131.18')
seq = seq.replace('K','146.19')
seq = seq.replace('M','149.21')
seq = seq.replace('F','165.19')
seq = seq.replace('P','115.13')
seq = seq.replace('S','105.09')
seq = seq.replace('T','119.12')
seq = seq.replace('W','204.23')
seq = seq.replace('Y','181.19')
seq = seq.replace('V', '117.15')

seq= seq.apply(pd.to_numeric, errors='ignore')

seq['Sum'] = seq.sum(axis =1)
seq['subtract'] = subtract['subtract']
seq['mass'] = seq['Sum'] - seq['subtract']

monoiso = pd.DataFrame()
monoiso['Monoisotopic Mass'] = seq['mass']
print(monoiso)