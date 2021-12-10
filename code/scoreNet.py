import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier

rrmatTrain = pd.read_csv("rrmatTrain.csv",header=None)
rrmatTest = pd.read_csv("rrmatTest.csv",header=None)

y = rrmatTrain[50]
del rrmatTrain[50]
X = rrmatTrain


regr = MLPRegressor(solver="sgd", alpha=0.001, hidden_layer_sizes=(25,10,3), random_state=1, activation='logistic',max_iter=1000)
regr.fit(X,y)

clf = MLPClassifier(solver="adam", alpha=0.001, hidden_layer_sizes=(25,10,3), random_state=1, activation='logistic',max_iter=1000)
clf.fit(X,y)

z = rrmatTest[50]
del rrmatTest[50]
D = rrmatTest

