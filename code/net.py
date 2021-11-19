import math
import csv
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

#Organising data

rrmat = pd.read_csv("rrmat.csv",header=None)

y = np.array([rrmat[50]]).T
del rrmat[50]
X = np.array(rrmat)

def act(z):
    return 1/(np.exp(-1*z)+1)

def is_Valid(M,n,k):
    if len(M) != k:
        return False
    else:
        for i in M:
            if len(i) != n:
                return False
        return True

def next_layer(W, a, b):
    '''
    Takes in a weight matrix W, the current layer of values, a, and the vector of biases. Outputs the vector of 
    values corresponding to the next layer in the network.
    '''
    if is_Valid(W,len(a),len(b)):
        A = []
        for row in W:
            sum = 0
            for element in row:
                sum += element*a[row.index(element)]
            A.append(sum)
        for a in A:
            A[A.index(a)]= act(a + b[A.index(a)])
        return A
    else:
        return False


errorVals = []
alpha = 0.2
K = 3 #Number of hidden layers
hW = 2*np.random.random((X.shape[1]+1,K))-1 #Hidden weights
oW = 2*np.random.random((K+1,y.shape[1]))-1 #Output weights

#Backpropogation
for i in range(1000):
    #Feedforward phase
    inputLayerOutputs = np.hstack((np.ones((X.shape[0],1)), X))
    hiddenLayerOutputs = np.hstack((np.ones((X.shape[0], 1)), act(np.dot(inputLayerOutputs, hW))))
    output = np.dot(hiddenLayerOutputs,oW)

    #Error calculations
    error = output - y
    hError = hiddenLayerOutputs[:,1:]*(1-hiddenLayerOutputs[:,1:])*np.dot(error,oW.T[:,1:]) #errors in the hidden layer
    errorVals.append(np.average(error**2)/(2*len(y)))
    #Partial derivatives
    hiddenPD = inputLayerOutputs[:,:,np.newaxis]*hError[:,np.newaxis,:]
    outputPD = hiddenLayerOutputs[:,:,np.newaxis]*output[:,np.newaxis,:]

    totHidGrad = np.average(hiddenPD,axis=0)
    totOutGrad = np.average(outputPD,axis=0)

    #Updated weights
    hW += -alpha*totHidGrad
    oW += -alpha*totOutGrad

plt.plot(errorVals)
plt.show()