#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This code was modified from code written by Antonia Hadjimichael
(https://github.com/antonia-had/Magnitude_varying_sensitivity_analysis).
"""

def magnitude_perc_plots(sim, obs):
    
    import numpy as np
    import matplotlib
    from matplotlib import pyplot as plt
    
    runs = len(sim.index)

    # convert pandas dataframe to numpy matrix
    obs = obs.to_numpy()[:, 1]
    sim = sim.to_numpy()
    
    # plot historical series
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(np.arange(len(obs)), obs, c = 'black')
    ax.set_ylabel('Observation Value', fontsize = 15)
    ax.set_xlabel('Observation', fontsize = 15)
    # plt.savefig('output/plots/magnitude_perc/observation_data.png')
    plt.savefig('output/plots/magnitude_perc/observation_data.eps', format = 'eps', dpi = 1000)


    # sort historical data in percentiles of magnitude
    obs_sort = np.sort(obs)
    
    # estimate percentiles according to record length
    P = np.arange(1., len(obs) + 1) * 100 / len(obs)
    
    # Plot historical percentiles of magnitude
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(P, obs_sort, c = 'black')
    ax.set_ylabel('Observation Value', fontsize = 12)
    ax.set_xlabel('Magnitude Percentile', fontsize = 12)
    # plt.savefig('output/plots/magnitude_perc/historical_data_percentiles.png')
    plt.savefig('output/plots/magnitude_perc/historical_data_percentiles.eps', format = 'eps', dpi = 1000)


    # sort simulation data
    sim_sort = np.zeros_like(sim)
    
    for j in range(runs):
        sim_sort[j, :] = np.sort(sim[j, :])

    # plot historical percentiles of magnitude and sampled series        
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    for j in range(runs):
        ax.plot(P, sim_sort[j, :], c = '#4286f4')
    ax.plot(P, sim_sort[0, :], c = '#4286f4', label = 'Simulation')            
    ax.plot(P, obs_sort, c = 'black', label = 'Observation')
    ax.legend(loc = 'upper left')
    ax.set_ylabel('Observation Value', fontsize = 12)
    ax.set_xlabel('Magnitude Percentile', fontsize = 12)
    # plt.savefig('output/plots/magnitude_perc/experiment_data_all.png')
    plt.savefig('output/plots/magnitude_perc/experiment_data_all.eps', format = 'eps', dpi = 1000)


    # plot range of experiment outputs
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.fill_between(P, np.min(sim_sort[:, :], 1), np.max(sim_sort[:, :], 1), color = '#4286f4', alpha = 0.1, label = 'Simulation')
    ax.plot(P, np.min(sim_sort[:, :], 1), linewidth = 0.5, color = '#4286f4', alpha = 0.3)
    ax.plot(P, np.max(sim_sort[:, :], 1), linewidth = 0.5, color = '#4286f4', alpha = 0.3)        
    ax.plot(P, obs_sort, c = 'black', label = 'Observation')
    ax.legend(loc = 'upper left')
    ax.set_ylabel('Observation Value', fontsize = 12)
    ax.set_xlabel('Magnitude Percentile', fontsize = 12)
    # plt.savefig('output/plots/magnitude_perc/experiment_data_range.png') 
    plt.savefig('output/plots/magnitude_perc/experiment_data_range.eps', format = 'eps', dpi = 1000)


    # to plot output density of experiment we need an array of percentiles
    p = np.arange(100, 0, -10)

    # Function to calculate custom transparency for legend purposes
    def alpha(i, base = 0.2):
        l = lambda x: x+base-x*base
        ar = [l(0)]
        for j in range(i):
            ar.append(l(ar[-1]))
        return ar[-1]

    handles = []
    labels=[]
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    for i in range(len(p)):
        ax.fill_between(P, np.min(sim_sort[:, :], 1), np.percentile(sim_sort[:, :], p[i], axis = 1), color='#4286f4', alpha = 0.1)
        ax.plot(P, np.percentile(sim_sort[:, :], p[i], axis = 1), linewidth = 0.5, color = '#4286f4', alpha = 0.3)
        handle = matplotlib.patches.Rectangle((0, 0), 1, 1, color = '#4286f4', alpha = alpha(i, base = 0.1))
        handles.append(handle)
        label = "{:.0f} %".format(100 - p[i])
        labels.append(label)
        
    ax.plot(P, obs_sort, c = 'black', linewidth = 2, label = 'Historical record')
    ax.set_xlim(0, 100)
    ax.legend(handles = handles, labels = labels, framealpha = 1, fontsize = 8, loc = 'upper left', title = 'Frequency in experiment', ncol = 2)
    ax.set_xlabel('Magnitude Percentile', fontsize = 12)
    # plt.savefig('output/plots/magnitude_perc/experiment_data_density.png')
    plt.savefig('output/plots/magnitude_perc/experiment_data_density.eps', format = 'eps', dpi = 1000)

    
    