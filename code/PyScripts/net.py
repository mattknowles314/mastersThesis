import math
import csv
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

#Organising data

rrmatTrain = pd.read_csv("rrmatTrain.csv",header=None)
rrmatTest = pd.read_csv("rrmatTest.csv",header=None)

y = np.array([rrmatTrain[50]]).T
del rrmatTrain[50]
X = np.array(rrmatTrain)

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


alpha = 0.2
K = 3 #Number of hidden layers
hW = 1000*np.random.random((X.shape[1]+1,K)) #Hidden weights
oW = 1000*np.random.random((K+1,y.shape[1])) #Output weights

print("Performing Backpropogation...")
#Backpropogation
for i in range(100):
    #Feedforward phase
    inputLayerOutputs = np.hstack((np.ones((X.shape[0],1)), X))
    hiddenLayerOutputs = np.hstack((np.ones((X.shape[0], 1)), act(np.dot(inputLayerOutputs, hW))))
    output = np.dot(hiddenLayerOutputs,oW)

    #Error calculations
    error = output - y
    hError = hiddenLayerOutputs[:,1:]*(1-hiddenLayerOutputs[:,1:])*np.dot(error,oW.T[:,1:]) #errors in the hidden layer

    #Partial derivatives
    hiddenPD = inputLayerOutputs[:,:,np.newaxis]*hError[:,np.newaxis,:]
    outputPD = hiddenLayerOutputs[:,:,np.newaxis]*output[:,np.newaxis,:]

    totHidGrad = np.average(hiddenPD,axis=0)
    totOutGrad = np.average(outputPD,axis=0)

    #Updated weights
    hW += -alpha*totHidGrad
    oW += -alpha*totOutGrad


z = np.array([rrmatTest[50]]).T
del rrmatTest[50]
D = np.array(rrmatTest)

predVals = []

print("Predicting...")

for j in range(len(z)):
    inputLayerOutputs = D[1]
    hiddenLayerOutputs = np.hstack((np.ones((D.shape[0], 1)), act(np.dot(inputLayerOutputs, hW))))
    output = np.dot(hiddenLayerOutputs,oW)
    predVals.append(np.average(output))

#plt.scatter([x for x in range(len(z))],z,alpha=0.5)
#plt.scatter([x for x in range(len(predVals))],predVals,alpha=0.5)
#plt.savefig("netplot.png")  

print("Output After Training: \n{}".format(output))
print("Process Complete")