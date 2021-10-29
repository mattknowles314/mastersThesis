import math
import csv
import pandas as pd

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

def next_layer(W, a, b):
    '''
    Takes in a weight matrix W, the current layer of values, a, and the vector of biases. Outputs the vector of 
    values corresponding to the next layer in the network.
    '''
    if not is_Valid(W,len(a),len(b)):
        return False
    else:
        A = []
        for row in W:
            sum = 0
            for element in row:
                sum += element*a[row.index(element)]
            A.append(sum)
        for a in A:
            A[A.index(a)]= act(a + b[A.index(a)])
        return A




W = [[1,2,3],[4,2,6]]
a = [6,7,9]
b = [1,1]

print(next_layer(W,a,b))