#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:05:26 2019

@author: catiefinkenbiner
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error

def run_function(x,a,b,c,d):
    y = (x**a+x*b+c)
    return y

count = np.arange(1000)
df = np.zeros((count.size,7))
mu, sigma = 0, 1
output = run_function(0.50,np.random.normal(mu,sigma),np.random.normal(mu,sigma),
                      np.random.normal(mu,sigma),np.random.normal(mu,sigma))

for i in np.arange(len(count)):
    x = 0.50
    df[i,0] = output
    df[i,1] = i
    df[i,2] = np.random.normal(mu,sigma)
    df[i,3] = np.random.normal(mu,sigma)
    df[i,4] = np.random.normal(mu,sigma)
    df[i,5] = np.random.normal(mu,sigma)
    
    df[i,6] = run_function(x,df[i,2],df[i,3],df[i,4],df[i,5])

def make_figs():    
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
    

plt.figure()
make_figs()
#plt.savefig('demo_fig1.png',dpi=400)
df = pd.DataFrame(df,columns=['observation', 'model #', 'parameter1','parameter2',
                              'parameter3','parameter4','prediction'])
#df.to_csv('dummy_data.csv')


    
