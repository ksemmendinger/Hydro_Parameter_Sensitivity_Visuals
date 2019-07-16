#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:15:58 2019

@author: kylasemmendinger
"""

'''
This script calculates Sobol first-, second-, and total order sensitivity indices 
based on the SAlib (https://github.com/SALib) and creates radial convergence plots 
based on a script written by Antonia Hadjimichael (https://github.com/antonia-had).

'''

def objective_function_sobol(problem, OF):
    
    from SALib.analyze import sobol
    import numpy as np
    import csv
    
    # initialize an empty list to save Sobol Indices
    results = []
    
    # loop through each OF and calculate the Sobol Indices for each parameter
    for j in np.arange(len(OF.columns)):
        
        # subset the OF of interest
        Y = np.array(OF.iloc[:, j])
         
        # calculate Sobol indices
        SI = sobol.analyze(problem, Y, calc_second_order = True, num_resamples = 100, conf_level = 0.95, print_to_console = False)
        
        # hard code any negative indices to 0
        SI['S1'][SI['S1'] < 0] = 0
        SI['ST'][SI['ST'] < 0] = 0
        
        # save output to text file
        keys = SI.keys()
                    
        with open('output/sobol_' + OF.columns[j] + '.csv', 'w') as csvfile:
            fieldnames = keys
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow(SI)

        # save in results list
        results.append([SI])
        
    return results