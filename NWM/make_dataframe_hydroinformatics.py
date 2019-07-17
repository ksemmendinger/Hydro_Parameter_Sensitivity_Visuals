#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:39:49 2019

@author: catiefinkenbiner
"""

import pandas as pd
import matplotlib.pyplot as plt

folder = '/Volumes/Seagate Backup Plus Drive/HydroInformatics/20190701/sipsey_wilderness_restart_run/'

def make_df(folder):    
    
    ## Read OUTPUTS ---------------------------------------------------------------
    data_dir = folder+'frxst_pts_out.txt'
    df_streamflow_locs = pd.read_csv(data_dir,header=None,delimiter=',')
    df_streamflow_locs.columns=['TimeFromStart','Time','station','longitude','latitude','q_cms','q_cfs','stage']
    
    plt.plot(df_streamflow_locs['TimeFromStart']/(60*60*24),df_streamflow_locs['q_cms'],'r-',label='q_cms')
    plt.title('Station ID:'+str(df_streamflow_locs['station'][0]))
    plt.xlabel('days')
    plt.ylabel('streamflow (cms)')
    
    return df_streamflow_locs

final_df = make_df(folder)
# final_df.to_csv('NWM_data_20190701.csv')

## Let's make an input file for WRES
# start_date, value_date, variable_name, location, measurement_unit, value
wres_df = final_df.filter(['Time','Time','q_cms','station','q_cms','q_cms']).copy()
wres_df.columns=['start_date', 'value_date', 'variable_name', 'location', 'measurement_unit', 'value']
wres_df['start_date'] = '2010-01-01 01:00:00'
#wres_df['value_date'].iloc[0]
wres_df['variable_name'] = 'SQIN'
wres_df['measurement_unit'] = 'CMS'

wres_df.to_csv('wres_input.csv',index=False)