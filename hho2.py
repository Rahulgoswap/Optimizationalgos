# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math
import random

def initializer(N, dim, up, down):
       
    x = np.random.rand(N, dim)
    x = np.multiply(x,up-down)+down
    
    return x

def f5(x):
    dim=x.shape[0];
    o=100*(np.power(x[1:dim]-np.power(x[0:dim-1],2),2))+np.power(x[0:dim-1]-1,2);
    return sum(o)

def HHO(N,T,lb,ub,dim):
    print("Optimization is underway")
    Rabbit_Location =np.zeros(dim)
    Rabbit_Energy = math.inf
    
    X = initializer(N,dim,ub,lb)
    CNVG = np.zeros(T,dtype=int)
    
    t=0
    
    
 
    while(t<T):
        fu=np.zeros((X.shape[0],X.shape[1]),dtype=int)
        fl=np.zeros((X.shape[0],X.shape[1]),dtype=int)
        fu.reshape(X.shape[0],X.shape[1])
        fl.reshape(X.shape[0],X.shape[1])
        flu = np.zeros((X.shape[0],X.shape[1]),dtype=int)
        fl.reshape(X.shape[0],X.shape[1])
        for i in range(X.shape[0]):
            
           """Check Boundaries"""
           """Loope Otimization Required"""
           for j in range(X.shape[1]):
                if(X[i][j]<lb):
                    fl[i][j]=1
                elif(X[i][j]>ub):
                    fu[i][j]=1
                flu[i][j] = fl[i][j]+fu[i][j]
                if(flu[i][j]==0):
                    flu[i][j]=1
                else:
                    flu[i][j]=0
             
           xnew = np.multiply(X,flu)+np.multiply(ub,fu)+np.multiply(lb,fl)
           """Using xnew from here on"""
           """ CHeck Fitness"""
           fitness = f5(xnew[i,:])
           print(fitness)
         
            
             
            
                
