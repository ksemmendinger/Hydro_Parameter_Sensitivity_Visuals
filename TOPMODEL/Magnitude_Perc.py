#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:07:30 2019

@author: kylasemmendinger
"""

# import python libraries
import pandas as pd
import os

# back out a directory to load python functions from "Scripts" folder
org_dir_name = os.path.dirname(os.path.realpath('Magnitude_Perc.py'))
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath('Magnitude_Perc.py')))
os.chdir(parent_dir_name + "/Scripts")

# load python functions from ‘Scripts’ folder
import magnitude_percentile_plots

# move back into case study 0 folder
os.chdir(org_dir_name)

# load in model simulationsand observation data
sim = pd.read_csv("input/simulation_ts.csv", index_col = 0)
obs = pd.read_csv("input/observation_ts.csv")

# create magnitude percentile plots from observation and simulation time series data
magnitude_percentile_plots.magnitude_perc_plots(sim, obs)
