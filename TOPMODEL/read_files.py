#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:16:06 2019

@author: catiefinkenbiner
"""

import numpy as np
import pandas as pd

folder = '/Users/catiefinkenbiner/Documents/Summer Institute/CaseStudies/Scaling/'

df_parms = pd.read_csv(folder+'Table1_hydroinfo.csv', index_col=0)
df_of = pd.DataFrame({'NSE':df_parms.iloc[:,10]})
df_parms = df_parms.drop(columns=['NSE'])
df_sims = pd.read_csv(folder+'Table2_hydroinfo.csv', index_col=0)

runs = 5000
bins = 100
color1 = 'b'
color2 = 'k'
color3 = 'r'

tolerance_nse = 0.0
runABC(df_parms,df_of,runs,bins,color1,color2,'NSE_'+str(tolerance_nse))

tolerance_nse = 0.15
runABC(df_parms,df_of,runs,bins,color1,color3,'NSE_'+str(tolerance_nse))

#df_parms.to_csv('parameters.csv',index=False)
#df_of.to_csv('objective_function_NSE.csv',index=False)
