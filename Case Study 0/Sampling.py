#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:56:56 2019

@author: kylasemmendinger
"""
# import python libraries
from SALib.sample import saltelli
import pandas as pd

# Define the model inputs
problem = {
    'num_vars': 11,
    'names': ['w', 'n_imperv', 'n_perv', 's_imperv', 's_perv', 'k_sat', 'per_routed', 'cmelt', 'Tb', 'A1', 'B1'],
    'bounds': [[500, 1500], # meters
               [0.01, 0.2],
               [0.01, 0.2],
               [0, 10],
               [0, 10],
               [0.01, 10],
               [0, 100],
               [0, 4],
               [-3, 3],
               [0.0001, 0.01],
               [1, 3]]
}

# Generate samples
param_values = saltelli.sample(problem, 1000)

param_values = pd.DataFrame(param_values)
param_values.columns = problem['names']
param_values.to_csv("input/params.csv", index = False)

