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
import sobol
import ols
import radial_conv_plots
import magnitude_percentile_plots

# move back into case study 0 folder
os.chdir(org_dir_name)

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

# load in model parameter sets (Saltelli sampled) and objective function values
pars = pd.read_csv("input/params.csv", header = 0)
OF = pd.read_csv("input/OF_values.csv")

# save the parameter names
param_names = problem['names']

# calculate Sobol first-, second-, and total order indices --> MUST BE BASED ON SALTELLI SAMPLING SCHEME
results_SI = []
results_SI = sobol.objective_function_sobol(problem, OF)

# create radial convergence plots based on results_SI
radial_conv_plots.radial_conv_plots(problem, results_SI, OF)

# calculate delta indices and sobol first-order indices
results_delta = []
results_delta = delta.objective_function_delta(problem, pars, OF)

# calculate R^2 from OLS regression
results_R2 = []
results_R2 = ols.objective_function_OLS(OF, pars, param_names)