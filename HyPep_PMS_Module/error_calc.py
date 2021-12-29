# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 12:08:49 2021

@author: lawashburn
"""
import numpy as np
import pandas as pd
from mass_query import masses
from mass_query import mass_pos

error = pd.DataFrame()
error['allowed masses'] = mass_pos
error['experimental masses'] = masses
closest_mass_indices = np.argmin(np.abs(masses.values.reshape(1, -1) - mass_pos.values.reshape(-1, 1)), axis=1) 
error['closest_mass'] = closest_mass_indices
print(error)