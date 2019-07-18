#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:15:01 2019

@author: kylasemmendinger
"""

def objective_function_delta(problem, pars, OF):
    
    from SALib.analyze import delta
    import numpy as np
    import csv
    
    # convert pandas dataframe to numpy matrix
    params = pars.to_numpy()

    # initialize an empty list to save Sobol Indices
    results = []
    
    # loop through each OF and calculate the Delta Indices and Sobol first-order index for each parameter
    for j in np.arange(len(OF.columns)):
        
        # subset the OF of interest
        Y = np.array(OF.iloc[:, j])
         
        # calculate Sobol indices
        DI = delta.analyze(problem, params, Y)
        
        # hard code any negative indices to 0
        DI['delta'][DI['delta'] < 0] = 0
        DI['S1'][DI['S1'] < 0] = 0
        
        # save output to text file
        keys = DI.keys()
                    
        with open('output/raw/delta_' + OF.columns[j] + '.csv', 'w') as csvfile:
            fieldnames = keys
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow(DI)
        
        # save in results list
        results.append([DI])
        
    return results