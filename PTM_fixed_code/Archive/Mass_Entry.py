# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:50:34 2021

@author: lawashburn
"""
#Gives all masses of database entries
import csv
import pandas as pd
from PTM_sample_4 import query
from User_input import mass_sequence


#print(mass_sequence)
mass_sequence.set_index('Sequence', inplace=True) #set sequence column as the fixed row
#print(mass_sequence)

mass_dict = mass_sequence.to_dict()
