#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 08:11:03 2019

@author: catiefinkenbiner
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

def make_figure(x):
    plt.figure()
    for i in np.arange(x):
        plt.plot(np.arange(len(df_model.iloc[i,1:])),df_model.iloc[i,1:],'b-')
    plt.plot(np.arange(len(df_obs.iloc[:,1])),df_obs.iloc[:,1],'r-')
    plt.xticks(np.arange(0,4321,1000))
    plt.xlabel('time step')
    plt.ylabel('discharge cms')
    plt.tight_layout()
