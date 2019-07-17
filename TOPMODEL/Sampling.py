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
    'num_vars': 10,
    'names': ['qs0', 'lnTe', 'm', 'Sr0', 'Srmax', 'td', 'vch', 'vr', 'k0', 'CD'],
    'bounds': [[0, 0.00003],
               [-2, -0.5],
               [0.3, 1],
               [0.005, 0.2],
               [0.1, 1],
               [0, 0.5],
               [500, 2000],
               [500, 2000],
               [0.05, 0.2],
               [0, 10]]

}

# Generate samples
param_values = saltelli.sample(problem, 1000)

param_values = pd.DataFrame(param_values)
param_values.columns = problem['names']
param_values.to_csv("input/params.csv", index = False)

