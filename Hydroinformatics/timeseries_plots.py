#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:11:03 2019

@author: catiefinkenbiner
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

folder = '/Users/catiefinkenbiner/Documents/Summer Institute/CaseStudies/Hydroinformatics'
df_obs = pd.read_csv(folder+'/results/USGS_obs.csv')
df_model = pd.read_csv(folder+'/results/NWM_0.7.csv')

plt.figure()
plt.plot(df_obs['q_cms'],'r-',label='USGS')
plt.plot(df_model['q_cms'],'b-',label='NWM')
plt.legend()