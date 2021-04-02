#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:51:07 2021

@author: catiefinkenbiner
"""

# import python libraries
import pandas as pd
import numpy as np
import os
import matplotlib
import datetime as dt
from matplotlib import pyplot as plt

matplotlib.rcParams.update({'font.size': 14})

### Figure 2. Magnitude Percentile Plots
def make_fig2(timestamps, sim, obs):
    runs = len(sim.index)

    # convert pandas dataframe to numpy matrix
    x = len(obs.columns)
    if x != 1:
        obs = obs.to_numpy()[:, 1]
    else:
        obs = obs.to_numpy()    
    sim = sim.to_numpy()
    
    # plot historical series
    fig = plt.figure(figsize=(12,5))
    ax = fig.add_subplot(1, 2, 1)
    ax.plot(timestamps['x'], obs, c = 'black')
    ax.set_ylabel(r'Discharge $(cms)$', fontsize = 15)
    ax.set_ylim(0, 75)
    ax.tick_params(axis='x', labelrotation = 25)
    
    # sort historical data in percentiles of magnitude
    obs_sort = np.sort(obs)    
    # estimate percentiles according to record length
    P = np.arange(1., len(obs) + 1) * 100 / len(obs)    
    # sort simulation data
    sim_sort = np.zeros_like(sim)
    
    for j in range(runs):
        sim_sort[j, :] = np.sort(sim[j, :])

    # to plot output density of experiment we need an array of percentiles
    p = np.arange(100, 0, -10)

    # Function to calculate custom transparency for legend purposes
    def alpha(i, base = 0.2):
        l = lambda x: x+base-x*base
        ar = [l(0)]
        for j in range(i):
            ar.append(l(ar[-1]))
        return ar[-1]

    handles = [] ; labels=[]
    
    ax2 = fig.add_subplot(1, 2, 2)
    trans_sim_sort = np.transpose(sim_sort)
    
    for i in range(len(p)):
        ax2.fill_between(P, np.min(trans_sim_sort[:, :], 1), np.percentile(trans_sim_sort[:, :], p[i], axis = 1), color='#4286f4', alpha = 0.1)
        ax2.plot(P, np.percentile(trans_sim_sort[:, :], p[i], axis = 1), linewidth = 0.5, color = '#4286f4', alpha = 0.3)
        handle = matplotlib.patches.Rectangle((0, 0), 1, 1, color = '#4286f4', alpha = alpha(i, base = 0.1))
        handles.append(handle)
        label = "{:.0f} %".format(100 - p[i])
        labels.append(label)
        
    ax2.plot(P, obs_sort, c = 'black', linewidth = 2, label = 'Historical record')
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 75)
    ax2.legend(handles = handles, labels = labels, framealpha = 1, fontsize = 10, loc = 'upper left', title = 'Frequency in experiment', ncol = 2)
    ax2.set_ylabel(r'Discharge $(cms)$', fontsize = 15)
    ax2.set_xlabel('Magnitude Percentile', fontsize = 15)
    
    ax.text(dt.date(2013, 6, 15),70,'a)')
    ax2.text(90,70,'b)')
    plt.tight_layout()
    plt.savefig('JAWRA_Figures/Figure2_magnitude_percentile_plot.pdf', dpi = 1000)
    plt.savefig('JAWRA_Figures/Figure2_magnitude_percentile_plot.png', dpi = 1000)
    
def magnitude_perc_plots_fig2():
    sim = pd.read_excel("input/simulation_ts.xlsx", index_col = 0)
    obs = pd.read_csv("input/observation_ts.csv")
    timestamps = pd.read_csv("input/timestamps.csv")
    timestamps['x'] = pd.to_datetime(timestamps['x'], format='(%m/%d/%y %H:%M:%S)')
    
    make_fig2(timestamps, sim, obs)
    

### Figure 3. ABC Results

def make_fig3(df_parms,df_OFs,runs,bins):
    bayes_approx = pd.read_csv('output/bayes_parameters_NSE.csv')
  
    ## Histogram of A1 parameter
    fig = plt.figure(figsize=(12,5))
    ax = fig.add_subplot(1, 2, 1)
    
    alpha=0.50 #fade
    ax = df_parms['A1'].plot.hist(bins=bins,alpha=alpha,color='b',linewidth=4) 
    ax = bayes_approx['A1'].plot.hist(bins=bins,alpha=alpha,color='k',linewidth=4)
    ax.set_xlabel('A1')
    ax.set_ylabel('Frequency')
    
    ax2 = fig.add_subplot(1, 2, 2)
    ax2 = df_parms['B1'].plot.kde(alpha=alpha,color='b',linewidth=4) 
    ax2 = bayes_approx['B1'].plot.kde(alpha=alpha,color='k',linewidth=4) 
    ax2.set_xlabel('B1')    
    ax2.set_ylabel('Density')
    plt.legend(['Model Output','ABC Results'],fancybox=True)

    ax.text(0.009,20,'a)')
    ax2.text(3.75,0.025,'b)')
    plt.tight_layout()
    plt.savefig('JAWRA_Figures/Figure3_abc.pdf', dpi = 1000)
    plt.savefig('JAWRA_Figures/Figure3_abc.png', dpi = 1000)
    
def ABC_plots_fig3():
    pars = pd.read_csv("input/params.csv", header = 0)
    pars.columns = ['w', 'n_imperv', 'n_perv', 's_imperv', 's_perv', 'k_sat', 'per_routed', 'cmelt', 'Tb', 'A1', 'B1']
    OF = pd.read_csv("input/OF_values.csv")
    
    make_fig3(pars, OF.iloc[:,-1], 24000, 100)

    
    
    
    