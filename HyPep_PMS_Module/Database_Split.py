# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:44:05 2021

@author: lawashburn
"""
#Organizes ptm info in dataframe
import pandas as pd
import numpy as np
from Execute2 import temp_df
#from PTM_sample_4 import query
from User_input2 import monoiso

df_seq = pd.DataFrame(temp_df) #convert temp df to permanent
#df_seq.set_index('entry', inplace=True) #set entry column as the fixed row

#print(df_seq.info()) #This tells us the data type of the df

df_seq['mass'] = pd.to_numeric(df_seq['mass']) #converts all values in 'mass' column of df from object to int

#df_seq['mass'] = df_seq['mass'] + 1 #Adds value to each item in column 'mass'

#or a in df_seq['entry']:
#   df_seq['mass'] = df_seq['mass'] + (mass_sequence[mass_sequence['Sequence']==a]['Mass'])
#rint('after add', df_seq)

#first_column = df_seq.iloc[:,0]


#df_seq['Precursor'] = [642 if ele == 'KGTLPK' else 0 for ele in df_seq['entry']]
#print(df_seq)

df_seq['Precursor'] = df_seq['entry'] #duplicating the entry values into a new column called 'precursor'


Pre = pd.DataFrame()
Pre['Precursor'] = df_seq['Precursor']

Pre = Pre['Precursor'].apply(lambda x: pd.Series(list(x)))
Sub = pd.DataFrame()
Sub = Pre
Pre = Pre.astype(str) # changes all mass values out for strings for replacement to happen

Pre = Pre.replace('A','89.10')
Pre = Pre.replace('R','174.20')
Pre = Pre.replace('N','132.12')
Pre = Pre.replace('D','133.11')
Pre = Pre.replace('C','121.16')
Pre = Pre.replace('E','147.13')
Pre = Pre.replace('Q','146.15')
Pre = Pre.replace('G','75.07')
Pre = Pre.replace('H','155.16')
Pre = Pre.replace('O','131.13')
Pre = Pre.replace('I','131.18')
Pre = Pre.replace('L','131.18')
Pre = Pre.replace('K','146.19')
Pre = Pre.replace('M','149.21')
Pre = Pre.replace('F','165.19')
Pre = Pre.replace('P','115.13')
Pre = Pre.replace('S','105.09')
Pre = Pre.replace('T','119.12')
Pre = Pre.replace('W','204.23')
Pre = Pre.replace('Y','181.19')
Pre = Pre.replace('V', '117.15')

Pre= Pre.apply(pd.to_numeric, errors='ignore')

Pre['Sum'] = Pre.sum(axis =1) #prelim mass

Pre_del = Pre[Pre.columns.difference(["Sum"])]
Pre = Pre.drop(Pre_del, axis=1)

Sub = Sub.astype(str)

Sub = Sub.replace('A','1')
Sub = Sub.replace('R','1')
Sub = Sub.replace('N','1')
Sub = Sub.replace('D','1')
Sub = Sub.replace('C','1')
Sub = Sub.replace('E','1')
Sub = Sub.replace('Q','1')
Sub = Sub.replace('G','1')
Sub = Sub.replace('H','1')
Sub = Sub.replace('O','1')
Sub = Sub.replace('I','1')
Sub = Sub.replace('L','1')
Sub = Sub.replace('K','1')
Sub = Sub.replace('M','1')
Sub = Sub.replace('F','1')
Sub = Sub.replace('P','1')
Sub = Sub.replace('S','1')
Sub = Sub.replace('T','1')
Sub = Sub.replace('W','1')
Sub = Sub.replace('Y','1')
Sub = Sub.replace('V','1')

Sub= Sub.apply(pd.to_numeric, errors='ignore')

Sub['Subtract'] = Sub.sum(axis =1) #prelim mass
Sub_del = Sub[Sub.columns.difference(["Subtract"])]
Sub = Sub.drop(Sub_del, axis=1)
Sub['Amt Sub'] = ((Sub['Subtract'] * 18) - 18)
Monoisotopic = pd.DataFrame()
Monoisotopic['Mass'] = Pre['Sum'] - Sub['Subtract']

df_seq['Monoisotopic'] = Monoisotopic['Mass']
df_seq['mass_pos'] = df_seq['mass'] + df_seq['Monoisotopic']

df_seq2 = df_seq