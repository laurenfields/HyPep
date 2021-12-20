# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 14:28:45 2021

@author: lawashburn
"""

#PMS module
import csv
import pandas as pd


path = input('Enter path to experimental .csv: ')
sequence = pd.read_csv(path)

db_path = input('Enter path to database .csv: ')
db_sequence = pd.read_csv(db_path)

search = input('Enter search type: high, medium, low: ')
search_type = str(search)

db_high_list = []
seq_high_list = []
db_mid_list = []
seq_mid_list = []
db_low_list = []
seq_low_list = []
if search_type == 'high':
    db_high_list.append(db_sequence)
    seq_high_list.append(sequence)
    print('High is noted')
if search_type == 'medium':
    db_mid_list.append(db_sequence)
    seq_mid_list.append(sequence)
    print('Medium is noted')
if search_type == 'low':
    db_low_list.append(db_sequence)
    seq_low_list.append(sequence)
    print('Low is noted')

