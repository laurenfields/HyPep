# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:33:49 2021

@author: lawashburn
"""

from User_input import *
from User_input2 import simple_out_mass_match
from User_input2 import complex_out_mass_match
from User_input2 import out_ptm_match
import datetime
current_time = datetime.datetime.now()
import pandas as pd

analysis_type = input('Enter analysis type: Simple or Complex: ')
print(current_time)
if analysis_type == 'complex':
    from PTM_report import ptm_report_df
    from mass_query import df_seq2
    print('df seq 2 from user export',df_seq2)
    df_seq2.to_csv(complex_out_mass_match, index = False)
    ptm_report_df.to_csv(out_ptm_match, index = False) 
if analysis_type == 'simple':
    from Simple_PMS import monoiso
    monoiso.to_csv(simple_out_mass_match, index = False)
print(current_time)
print('Analysis Complete')
