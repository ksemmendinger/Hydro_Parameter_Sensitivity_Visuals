import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

'''
Approximate Baysian Calculation requires:
    1) observation dataset (df_obs)
    2) parameter sets (df_parms)
    3) model output (df_model)
    4) objective functions (df_OFs)
    5) tolerance
    6) number of model runs
'''

def approx_bayes_calc_OF(parms,OFs,simulations):
    keep_nse = []
    for i in np.arange(simulations):
        # User can redefine tolerance and OF here
        if OFs.iloc[i,0] >= tolerance_nse:
            keep_nse.append(parms.iloc[i])        
    return keep_nse

def make_histograms(df_parms,bayes_approx,bins,alpha,cc1,cc2,parameters,metric):
    plt.figure(figsize=(15,12))
    gridsize = math.ceil((np.sqrt((df_parms.iloc[0,:]).size))) # graph columns
    
    for col in np.arange(1,((df_parms.iloc[0,:]).size)+1):
        plt.subplot(gridsize-1,gridsize,col)
        ax = df_parms.iloc[:,col-1].plot.hist(bins=bins,alpha=alpha,color=cc1,linewidth=4)    
        ax = bayes_approx.iloc[:,col-1].plot.hist(bins=bins,alpha=alpha,color=cc2,linewidth=4)
        ax.set_xlabel(str(parameters[col-1]))    
    plt.legend(['Output','ABC'],fancybox=True)
    plt.tight_layout() 
    plt.savefig('output/plots/ABC/'+metric+'_histogram.png',dpi=1000)

def make_cdfs_pdfs(df_parms,bayes_approx,bins,alpha,cc1,cc2,parameters,metric):
    plt.figure(figsize=(15,12))
    gridsize = math.ceil((np.sqrt((df_parms.iloc[0,:]).size)))
    
    for col in np.arange(1,((df_parms.iloc[0,:]).size)+1):
        plt.subplot(gridsize-1,gridsize,col)
        ax = df_parms.iloc[:,col-1].plot.hist(cumulative=True, density=1,bins=bins,alpha=alpha,color=cc1,linewidth=4)    
        ax = bayes_approx.iloc[:,col-1].plot.hist(cumulative=True, density=1,bins=bins,alpha=alpha,color=cc2,linewidth=4)
        ax.set_xlabel(str(parameters[col-1]))    
    plt.legend(['Output','ABC'],fancybox=True)
    plt.tight_layout() 
    plt.savefig('output/plots/ABC/'+metric+'_cdf.png',dpi=1000)
    
    plt.figure(figsize=(15,12))
    gridsize = math.ceil((np.sqrt((df_parms.iloc[0,:]).size)))
    
    for col in np.arange(1,((df_parms.iloc[0,:]).size)+1):
        plt.subplot(gridsize-1,gridsize,col)
        ax = df_parms.iloc[:,col-1].plot.kde(alpha=alpha,color=cc1,linewidth=4)    
        ax = bayes_approx.iloc[:,col-1].plot.kde(alpha=alpha,color=cc2,linewidth=4)
        ax.set_xlabel(str(parameters[col-1]))   
    plt.legend(['Output','ABC'],fancybox=True)
    plt.tight_layout() 
    plt.savefig('output/plots/ABC/'+metric+'_pdf.png',dpi=1000)

def runABC(df_parms,df_OFs,runs,bins,color1,color2,metric):
    # models with objective functions within tolerance thresholds
    results_nse = np.array(approx_bayes_calc_OF(df_parms,df_OFs,runs))

    # saves models with objective functions within tolerance thresholds
    bayes_approx_nse = pd.DataFrame(results_nse,columns=None)
    bayes_approx_nse.to_csv('output/bayes_parameters_NSE.csv',index=False)
    parameters = list(df_parms.columns.values)
    
    # print ABC results and make figures
    print('precent of models with NSE >= to',str(tolerance_nse),'are:',str(len(results_nse)/runs),'%')
    make_histograms(df_parms,bayes_approx_nse,bins,0.5,color1,color2,parameters,'NSE')
    make_cdfs_pdfs(df_parms,bayes_approx_nse,bins,0.5,color1,color2,parameters,'NSE')