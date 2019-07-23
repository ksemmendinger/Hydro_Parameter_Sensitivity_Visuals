#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:56:56 2019

@author: kylasemmendinger
"""

# import python libraries
import pandas as pd
import os

# back out a directory to load python functions from "Scripts" folder
org_dir_name = os.path.dirname(os.path.realpath('SensIndices_RCPlots.py'))
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath('SensIndices_RCPlots.py')))
os.chdir(parent_dir_name + "/Scripts")

# load python functions from ‘Scripts’ folder
import delta
import ols

# move back into case study 0 folder
os.chdir(org_dir_name)

# load in model parameters and OF values
pars = pd.read_csv("input/params.csv", index_col = 0)
OF = pd.read_csv("input/OF_values.csv")

# Define the model inputs
problem = {
    'num_vars': 10,
    'names': ['qs0', 'lnTe', 'm', 'Sr0', 'Srmax', 'td', 'vch', 'vr', 'k0', 'CD']

}

# save the parameter names
param_names = problem['names']

# calculate delta indices and sobol first-order indices
results_delta = []
results_delta = delta.objective_function_delta(problem, pars, OF)

# calculate R^2 from OLS regression
results_R2 = []
results_R2 = ols.objective_function_OLS(OF, pars, param_names)
