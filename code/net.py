import math
import csv
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

#Organising data

rrmat = pd.read_csv("rrmat.csv",header=None)
Y = []
for i in rrmat[50]:
    Y.append(i)

def act(z):
    return 1/(math.exp(-1*z)+1)

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

#Initialse random weights and biases

W = []

W.append([[random.uniform(-1,1) for x in range(0,50)] for y in range(0,25)])
b1 = [1 for x in range(0,25)]
W.append([[random.uniform(-1,1) for x in range(0,25)] for y in range(0,10)])
b2 = [1 for x in range(0,10)]
W.append([[random.uniform(-1,1) for x in range(0,10)] for y in range(0,3)])
b3 = [1 for x in range(0,3)]
W.append([random.uniform(-1,1) for y in range(0,3)])
b4 = [1 for x in range(0,3)]

def initialise():
    Errors = []
    for j in range(1436):
        a1 = next_layer(W[0],list((rrmat.iloc[j])[0:-1]),b1)
        a2 = next_layer(W[1],a1,b2)
        a3 = next_layer(W[2],a2,b3)
        a4 = np.dot(W[3],a3)
        Errors.append( 0.5*((a4-Y[j])**2))
    return Errors

def single_backprop():
    '''
    To test my own understanding of this, we perform backpropogation on ONE training example. 
    '''
    Errors = []
    Outputs = []
    Outputs.append(next_layer(W[0],list((rrmat.iloc[6])[0:-1]),b1))
    Outputs.append(next_layer(W[1],Outputs[0],b2))
    Outputs.append(next_layer(W[2],Outputs[1],b3))
    Outputs.append([np.dot(W[3],Outputs[2])])
    delta1m = 0.5*((Outputs[-1][0]-Y[6])**2)
    Errors.append([delta1m])
    for k in reversed(range(1,3)):
        errs = []
        for j in range(0,len(W[k])):
            o = Outputs[k][j]
            errs.append(o*(1-o)*np.dot(Outputs[k+1],Errors[(k+1)-3]))
        Errors.append(errs)
    
    #need to do the partial differentiations next.