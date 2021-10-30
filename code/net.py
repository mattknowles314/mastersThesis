import math
import csv
import pandas as pd
import random
import numpy as np

#Organising data

rrmat = pd.read_csv("rrmat.csv",header=None)
Y = []
for i in rrmat[50]:
    Y.append(i)

def act(z):
    return math.tanh(z)

def is_Valid(M,n,k):
    if len(M) != k:
        return False
    else:
        for i in M:
            if len(i) != n:
                return False
        return True

def huber(y1,y,delta=1.0):
    if (np.abs(y-y1)) <= delta:
        return 0.5*(y-y1)**2
    else:
        return delta*(np.abs(y-y1)-0.5*delta)

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
W1 = [[random.randint(-1000,1000) for x in range(0,50)] for y in range(0,25)]
b1 = [1 for x in range(0,25)]
W2 = [[random.randint(-1000,1000) for x in range(0,25)] for y in range(0,10)]
b2 = [1 for x in range(0,10)]
W3 = [[random.randint(-1000,1000) for x in range(0,10)] for y in range(0,3)]
b3 = [1 for x in range(0,3)]
W4 = [random.randint(-1000,1000) for y in range(0,3)]
b4 = [1 for x in range(0,3)]

costs = []
def get_costs(X,y):
    a0 = list((rrmat.iloc[0])[0:-1])
    a1 = next_layer(W1,a0,b1)
    a2 = next_layer(W2,a1,b2)
    a3 = next_layer(W3,a2,b3)
    a4 = np.dot(W4,a3)
    costs.append((a4-y)**2)

i = 0
while i <= 1435:
    get_costs(list((rrmat.iloc[i])[0:-1]),Y[i])
    i+=1

print("Cost: ",np.average(costs))