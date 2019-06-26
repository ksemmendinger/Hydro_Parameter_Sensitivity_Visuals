#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:07:16 2019

@author: catiefinkenbiner
"""

# Read in NWM Output NetCDFs
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import glob, os
import xarray as xr

'''
Need from Hydroinformatics to populate .csv:
    1) All feature ids (for loop through them)
    2) input features/parameters that are changing
    3) observed data
'''

## Read INPUTS ----------------------------------------------------------------
data_dir = '/Users/catiefinkenbiner/Documents/Summer Institute/SI_Hydroinformatics/Hydroinformatics/results/config/DOMAIN/'
os.chdir(data_dir)

mfdataDIR = data_dir+'GWBUCKPARM.nc'
DS = xr.open_mfdataset(mfdataDIR)
coeff = (DS.Coeff.values)#.ravel() #read in soil propoerties


## Read OUTPUTS ---------------------------------------------------------------
data_dir = '/Users/catiefinkenbiner/Documents/Summer Institute/SI_Hydroinformatics/Hydroinformatics/results/'
os.chdir(data_dir)

mfdataDIR = data_dir+'*.CHRTOUT_DOMAIN1'
DS = xr.open_mfdataset(mfdataDIR)

time = (DS.sel(feature_id=18691203).time.values).ravel()

#dQ = (DS.streamflow.values)#.ravel() #read in streamflow
#To obtain the streamflow values for a specific reach (=feature_id):
model_streamflow = (DS.sel(feature_id=18691203).streamflow.values).ravel()
plt.figure()
plt.plot(time,model_streamflow,'r-')



