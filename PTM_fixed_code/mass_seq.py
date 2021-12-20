# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 09:58:10 2021

@author: lawashburn
"""

from User_input2 import monoiso
from Seq_format import seq
import pandas as pd

Seq_mass = pd.DataFrame()
Seq_mass = pd.concat([monoiso, seq], axis=1, join = 'inner')
