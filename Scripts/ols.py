#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:15:40 2019

@author: kylasemmendinger
"""

def objective_function_OLS(OF, pars, param_names):
    
    import statsmodels.api as sm
    import numpy
    import csv

    # initialize an empty list to a save r^2 coefficients
    results = []
    
    # loop through each OF and calculate the Delta Indices and Sobol first-order index for each parameter
    for j in numpy.arange(len(OF.columns)):
        
        results_by_OF = []
        
        for k in numpy.arange(len(pars.columns)):
            
            # subset parameter of interest
            exog = numpy.array(pars.iloc[:, k])
    
            # subset the OF of interest
            endog = numpy.array(OF.iloc[:, j])
             
            # fit OLS
            ols = sm.OLS(endog, exog)
             
            # save fitting results
            fit = ols.fit() 
            
            # pull out R^2 value
            results_by_OF.append([str([param_names[k] + '_' + OF.columns[j]]), fit.rsquared])
            results.append([str([param_names[k] + '_' + OF.columns[j]]), fit.rsquared])
            
        with open('output/ols_' + OF.columns[j] + '.csv', 'w') as resultFile:
            wr = csv.writer(resultFile, dialect = 'excel')
            wr.writerows(results_by_OF)

    return(results)