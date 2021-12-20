# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:16:43 2021

@author: lawashburn
"""

#These are all the values the user will input

import csv
import pandas as pd

mass_q_path = input('Enter path to mass query .csv: ')
#mass_q_path = r'C:\Users\lawashburn\Documents\HyPep_1.0\PTM_fixed_code\mass_query.csv'
mass_q_sequence = pd.read_csv(mass_q_path) #mass_q_sequence is the query
mass_q_sequence_simp = mass_q_sequence


tol_in = input('Enter error margin for mass matching: ')
#tol_in = 100
tol_in = int(tol_in)  #User defined tolerance value

path = input('Enter path to database sequence .csv: ')
#path = r"C:\Users\lawashburn\Documents\HyPep_1.0\PMS_20211220\PTM_fixed_code-20211220T153626Z-001\PTM_fixed_code\sequence2.csv"
sequence = pd.read_csv(path)



