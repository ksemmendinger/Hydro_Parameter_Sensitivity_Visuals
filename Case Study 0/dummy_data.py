#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:05:26 2019

@author: catiefinkenbiner
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy

def run_function(x,a,b,c,d):
    y = (x**a-x**b/.15+.6*x*c-d*4)
    return y   

def dummy_data(yesno=0):   
    count = np.arange(1000)
    df = np.zeros((count.size,7))
    mu, sigma = 0, 1
    output = np.random.normal(mu,sigma)

    for i in np.arange(len(count)):
        x = 0.50
        df[i,0] = output
        df[i,1] = i
        df[i,2] = np.random.normal(mu,sigma)
        df[i,3] = np.random.normal(mu,sigma)
        df[i,4] = np.random.normal(mu,sigma)
        df[i,5] = np.random.normal(mu,sigma)
        
        df[i,6] = run_function(x,df[i,2],df[i,3],df[i,4],df[i,5])

    print(np.mean(df[:,2]),np.std(df[:,2]))
    if yesno == 1:
        # plot bias
        plt.figure()
        plt.subplot(2,2,1)
        plt.plot(df[:,2],df[:,6]-df[:,0],'r.')
        plt.xlabel('parameter1')
        plt.ylabel('bias')
        plt.subplot(2,2,2)
        plt.plot(df[:,3],df[:,6]-df[:,0],'r.')
        plt.xlabel('parameter2')
        plt.ylabel('bias')
        plt.subplot(2,2,3)
        plt.plot(df[:,4],df[:,6]-df[:,0],'r.')
        plt.xlabel('parameter3')
        plt.ylabel('bias')
        plt.subplot(2,2,4)
        plt.plot(df[:,5],df[:,6]-df[:,0],'r.')
        plt.xlabel('parameter4')
        plt.ylabel('bias')
        plt.tight_layout()
        plt.savefig('demo_fig1.png',dpi=400)
        df = pd.DataFrame(df,columns=['observation', 'model #', 'parameter1','parameter2',
                                      'parameter3','parameter4','prediction'])
        df.to_csv('dummy_data.csv')
    
    # baysian stats on parameter distributions
    def compare_data_to_dist(x, mu_1, mu_2, sd_1, sd_2):
        ll_1 = []
        ll_2 = []
            
        ll_1 = np.log(scipy.stats.norm.pdf(x, mu_1, sd_1))         
        ll_2 = np.log(scipy.stats.norm.pdf(x, mu_2, sd_2))
        plt.figure()
        plt.plot(x,'k-ll_1,'r-',ll_2,'b-')

    compare_data_to_dist(df[:,2],.45,.56,1.1,.8)
    
dummy_data()    
