#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:57:45 2019

@author: catiefinkenbiner
"""
'''
Approximate Baysian Calculation requires:
    1) observation dataset (df_obs)
    2) parameter sets (df_parms)
    3) model output (df_model)
    4) tolerance
    5) number of model runs
'''
def approx_bayes_calc(obs,parms,models,simulations,tolerance):
    keep = []
    for i in np.arange((simulations)):
        # 1) Observed datasets has known mean and standard deviation
        obs_mu = obs.mean()
        obs_sigma = obs.std()
        # 2) Parameters (theta)
        theta = parms.iloc[i,1:]
        # 3) Calculate objective function (NSE)
        bias = (models.iloc[i,1:] - obs.iloc[0,1:])
        mse = (bias**2).sum() # mean-squared error
        nse = 1 - mse/((models.iloc[i,:]-obs_mu)**2).sum()# nash-sutcliffe efficiency
        # 4) Define tolerance and calculate
        if nse >= tolerance:
                keep.append(parms.loc[i])        
    return keep

def make_histograms(df_parms,bayes_approx,bins,alpha,cc1,cc2,parameters):
    plt.figure(figsize=(12,12))
    for col in np.arange(1,((df_parms.iloc[0,:]).size)):
        plt.subplot(4,3,col)
        ax = df_parms.iloc[:,col].plot.hist(bins=bins,alpha=alpha,color=cc1)    
        ax = bayes_approx.iloc[:,col].plot.hist(bins=bins,alpha=alpha,color=cc2)
        ax.set_xlabel(str(parameters[col]))    
    #plt.legend('Output','ABC')
    plt.tight_layout()   

def runABC(df_obs,df_parms,df_model,runs,tolerance,bins,color1,color2):
    df_obs = pd.read_csv(df_obs)
    df_parms = pd.read_csv(df_parms)
    df_model = pd.read_csv(df_model)
    results = np.array(approx_bayes_calc(df_obs,df_parms,df_model,runs,tolerance))
    print('precent of models with NSE >= to',str(tolerance),'are:',str(len(results)/runs),'%')
    bayes_approx = pd.DataFrame(results,columns=None)
    parameters = list(df_parms.columns.values)
    make_histograms(df_parms,bayes_approx,bins,0.5,color1,color2,parameters)