import math
import csv

n_layers = 5
m=50
l = 0
weights = [[] for x in range(1,n_layers)]
biases = [1 for x in range(1,n_layers)] #initialse all biases as 1

class perceptron:
    def __init__(self, inputVector, bias):
        self.iV = inputVector
        self.b = bias

def sig(z):
    return 1/(1+exp(-1*z))

def J(W,b):
    A = 0
    for i in range(1,m+1):
        A += abs(h(x[i])-y[i])^2
    
