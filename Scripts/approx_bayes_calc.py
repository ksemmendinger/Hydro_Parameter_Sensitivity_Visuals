#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:57:45 2019

@author: catiefinkenbiner
"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Approximate Baysian Calculation requires:
    1) observation dataset (df_obs)
    2) parameter sets (df_parms)
    3) model output (df_model)
    4) objective functions (df_OFs)
    5) tolerance
    6) number of model runs
'''

def make_histograms(df_parms,bayes_approx,bins,alpha,cc1,cc2,parameters,metric):
    plt.figure(figsize=(12,12))
    for col in np.arange(1,((df_parms.iloc[0,:]).size)+1):
        plt.subplot(4,4,col)
        ax = df_parms.iloc[:,col-1].plot.hist(bins=bins,alpha=alpha,color=cc1,linewidth=4)    
        ax = bayes_approx.iloc[:,col-1].plot.hist(bins=bins,alpha=alpha,color=cc2,linewidth=4)
        ax.set_xlabel(str(parameters[col-1]))    
    plt.legend(['Output','ABC'],fancybox=True)
    plt.tight_layout() 
    plt.savefig('output/plots/ABC/'+metric+'_histogram.png',dpi=1000)

def make_cdfs_pdfs(df_parms,bayes_approx,bins,alpha,cc1,cc2,parameters,metric):
    plt.figure(figsize=(12,12))
    for col in np.arange(1,((df_parms.iloc[0,:]).size)+1):
        plt.subplot(4,4,col)
        ax = df_parms.iloc[:,col-1].plot.hist(cumulative=True, density=1,bins=bins,alpha=alpha,color=cc1,linewidth=4)    
        ax = bayes_approx.iloc[:,col-1].plot.hist(cumulative=True, density=1,bins=bins,alpha=alpha,color=cc2,linewidth=4)
        ax.set_xlabel(str(parameters[col-1]))    
    plt.legend(['Output','ABC'],fancybox=True)
    plt.tight_layout() 
    plt.savefig('output/plots/ABC/'+metric+'_cdf.png',dpi=1000)
    
    plt.figure(figsize=(12,12))
    for col in np.arange(1,((df_parms.iloc[0,:]).size)+1):
        plt.subplot(4,4,col)
        ax = df_parms.iloc[:,col-1].plot.kde(alpha=alpha,color=cc1,linewidth=4)    
        ax = bayes_approx.iloc[:,col-1].plot.kde(alpha=alpha,color=cc2,linewidth=4)
        ax.set_xlabel(str(parameters[col-1]))   
    plt.legend(['Output','ABC'],fancybox=True)
    plt.tight_layout() 
    plt.savefig('output/plots/ABC/'+metric+'_pdf.png',dpi=1000)

def runABC(df_parms,df_OFs,runs,bins,color1,color2):
    # models with objective functions within tolerance thresholds
    #results_of1,results_of2,results_of3,results_of4 = np.array(approx_bayes_calc_OF(df_parms,df_OFs,runs))
    results = np.array(approx_bayes_calc_OF(df_parms,df_OFs,runs))
    
    ofs = list(df_OFs.columns.values)
    parameters = list(df_parms.columns.values)
    
    # saves models with objective functions within tolerance thresholds
    for i in np.arange(len(results)):
        bayes_approx_of = pd.DataFrame(results[i],columns=None)
        bayes_approx_of.to_csv('output/bayes_parameters_'+str(ofs[i])+'.csv',index=False)
    
        # print ABC results and make figures
        print('precent of models with '+str(ofs[i])+', tolerance = '+str(tolerances[i])+':',str(len(results[i])/runs),'%')
        make_histograms(df_parms,bayes_approx_of,bins,0.5,colors[0],colors[i+1],parameters,ofs[i])
        make_cdfs_pdfs(df_parms,bayes_approx_of,bins,0.5,colors[0],colors[i+1],parameters,ofs[i])

