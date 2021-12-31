import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import tensorflow as tf

rrmatTrain = pd.read_csv("rrmatTrain.csv",header=None)
rrmatTest = pd.read_csv("rrmatTest.csv",header=None)

y = rrmatTrain[50]
del rrmatTrain[50]
X = rrmatTrain

print(X.shape[1])

tf.keras.backend.clear_session()
tf.random.set_seed(60)

model=keras.models.Sequential([
    keras.layers.Dense(50,input_dim=X.shape[1], activation="relu"),
    keras.layers.Dense(50,input_dim=X.shape[1], activation="relu"),
    keras.layers.Dense(units=25,activation="relu"),
    keras.layers.Dense(units=25,activation="relu"),
    keras.layers.Dense(units=3,activation="relu"),
    keras.layers.Dense(units=1),
],name="Initial Model")

model.summary()