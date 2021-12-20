# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 13:44:18 2021

@author: lawashburn
"""

import pandas as pd
from mass_query import df_ptm_mass2
from PTM_report import df

mass_PTM = pd.DataFrame()
mass_PTM['PTM mass'] = df_ptm_mass2
#mass_PTM['PTMs'] = df_ptm_list
